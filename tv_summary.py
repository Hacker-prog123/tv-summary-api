def run_tv_summary(main_file_bytes, rr_file_bytes):
    from io import BytesIO
    import pandas as pd

    main_file = BytesIO(main_file_bytes)
    rr_file = BytesIO(rr_file_bytes)

    df = pd.read_excel(main_file, sheet_name="TV")
    df.columns = df.columns.str.strip()

    esn_df = pd.read_excel(main_file, sheet_name="ESN", usecols="B:E")
    rr_df_full = pd.read_excel(rr_file, sheet_name="Export")
    rr_df_full.columns = rr_df_full.columns.str.strip()

    def clean_esn(val):
        val = str(val).strip().replace("\n", "").replace("\r", "").replace("\xa0", "").replace(" ", "")
        if val.replace("-", "", 1).isdigit():
            return val
        return None

    # Clean ESNs in RR data
    rr_df_full["Engine Serial Number"] = rr_df_full["Engine Serial Number"].apply(clean_esn)

    # Match ESNs by week
    esn_df["Week"] = esn_df["Week"].fillna(method="ffill")
    current_week_esns = esn_df[esn_df["Week"].str.contains("Week", na=False)]["Engine Serial Number"].astype(str).str.strip().tolist()

    # Strip and clean columns in df
    df.columns = df.columns.str.strip()
    df["Engine Number (Ex)"] = df["Engine Number (Ex)"].astype(str).str.strip()

    # Classify delivery type
    def classify_delivery_type(row):
        if row["TV Clear"] == "Y":
            return "TV Delivered"
        elif row["TVR Gate Raise"] == 0:
            return "TV Delivered"
        elif row["TV Status"] == "Self Picked":
            return "Self Picked"
        else:
            return "Undelivered"

    # Assign 'Delivery Type' before filtering
    df["Delivery Type"] = df.apply(classify_delivery_type, axis=1)

    # Filter to current week only
    df_current_week = df[df["Engine Number (Ex)"].isin(current_week_esns)].copy()
    df_current_week["ESN"] = df_current_week["Engine Number (Ex)"]

    # Summary logic (example)
    tv_delivered = (df_current_week["Delivery Type"] == "TV Delivered").sum()
    self_picked = (df_current_week["Delivery Type"] == "Self Picked").sum()
    undelivered = (df_current_week["Delivery Type"] == "Undelivered").sum()

    return {
        "tv_delivered": int(tv_delivered),
        "self_picked": int(self_picked),
        "undelivered": int(undelivered),
        "status": "success"
    }
