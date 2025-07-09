{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": none,
   "id": "14aae29b-bc7b-4cd1-b9b3-2680985af1e8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on all addresses (0.0.0.0)\n",
      " * Running on http://127.0.0.1:10000\n",
      " * Running on http://192.168.130.99:10000\n",
      "Press CTRL+C to quit\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, request, jsonify\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route('/tvsummary', methods=['POST'])\n",
    "def tv_summary():\n",
    "    data = request.get_json()\n",
    "    tv = data.get(\"TV_Number\", \"N/A\")\n",
    "    return jsonify({\"message\": f\"Received TV Number: {tv}\"})\n",
    "\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(host='0.0.0.0', port=10000)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ba2a642c-1bf2-4188-8f4e-cd33b61372c0",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
