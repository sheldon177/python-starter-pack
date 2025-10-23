#print("5+2", 5+2)
#print("i like pizza\ni like rugby\ni like python") 
#print("c:\\\\\\user\\\\student\\desktop\\my_file") tu texstshi gvchirdeba "\" schirdeba damxmare\ rom imushavos
"""print("item\tquantity")
print("apple\t")
print("banana\t4") sami mdzime gvinda rom vwerot bevr linze komentari""" 

# user=int(input("add radius "))
# result=3.14*user**2
# print(result)


import requests
import json
import time
import datetime

# ---------------------------------------------------------------------------
# 1. --- CONFIGURATION: PASTE YOUR BROWSER TOKENS HERE ---
# ---------------------------------------------------------------------------
YOUR_SESSID = "PASTE_YOUR_SESSID_HERE"
YOUR_CSRF_AUTH_TOKEN = "PASTE_YOUR_CSRF_AUTH_TOKEN_HERE"


# ---------------------------------------------------------------------------

# Helper functions (get_csrf_token, get_trade_quote) remain the same
def get_csrf_token(session):
    try:
        response = session.get('https://iapi.kraken.com/api/internal/csrf/PTL')
        response.raise_for_status()
        token_data = response.json()
        csrf_token = token_data.get("result", {}).get("csrf_token")
        if not csrf_token:
            print("   -> Error: Could not find 'csrf_token' in the response.")
            return None
        print(f"   -> Success! Got CSRF Token.")
        return csrf_token
    except requests.exceptions.RequestException as e:
        print(f"   -> Error fetching CSRF token: {e}")
        return None


def get_trade_quote(session, csrf_token, amount_to_spend):
    url = "https://iapi.kraken.com/api/internal/trades/ptl?preferred_asset_name=new"
    payload = {"amount": str(amount_to_spend), "amount_asset": "spend", "spend_asset": "USDC", "receive_asset": "SOL"}
    session.headers.update({"x-csrf-token": csrf_token})
    try:
        response = session.post(url, json=payload)
        response.raise_for_status()
        quote_data = response.json().get("result", {})
        quote_id = quote_data.get("quote_id")
        if not quote_id:
            print("   -> Error: Could not get a quote_id from the response.")
            return None
        print(f"   -> Success! Got Quote ID: {quote_id}")
        return quote_id
    except requests.exceptions.RequestException as e:
        print(f"   -> Error getting trade quote: {e}")
        return None


def execute_trade(session, quote_id, csrf_token):
    url = f"https://iapi.kraken.com/api/internal/trades/ptl/{quote_id}"
    session.headers.update({"x-csrf-token": csrf_token})
    try:
        response = session.put(url, json={})
        response.raise_for_status()
        result = response.json()
        if result.get("result") and result["result"].get("status") == "executed":
            print("\n   -> ✅ SUCCESS: Trade execution confirmed!")
            return True
        else:
            print(f"\n   -> ⚠️ WARNING: Request sent, but status not 'executed'. Response: {result}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"\n   -> ❌ ERROR executing trade: {e.response.text}")
        return False


# This function contains the core trading logic for one attempt
def perform_trade_attempt():
    """Performs a single attempt to convert USDC to SOL. Returns True on success, False on failure."""
    print("--- Starting new trade attempt ---")
    s = requests.Session()
    s.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
        "Origin": "https://www.kraken.com", "Referer": "https://www.kraken.com/",
        "csrf-auth": YOUR_CSRF_AUTH_TOKEN, "Content-Type": "application/json", "x-korigin": "g2081"
    })
    s.cookies.set("SESSID", YOUR_SESSID)

    quote_csrf_token = get_csrf_token(s)
    if not quote_csrf_token: return False

    usdc_amount_to_spend = 1.0
    quote_id = get_trade_quote(s, quote_csrf_token, usdc_amount_to_spend)
    if not quote_id: return False

    s.headers.update({"x-initiated-through": "@frontend/cts-core"})

    print("   -> Fetching final CSRF token for execution...")
    execution_csrf_token = get_csrf_token(s)
    if not execution_csrf_token: return False

    return execute_trade(s, quote_id, execution_csrf_token)


# This is the main controller for scheduling and looping
def main():
    if YOUR_SESSID == "PASTE_YOUR_SESSID_HERE" or YOUR_CSRF_AUTH_TOKEN == "PASTE_YOUR_CSRF_AUTH_TOKEN_HERE":
        print("Please configure the script with your SESSID and csrf-auth token first.")
        return

    # --- SCHEDULING LOGIC ---
    now = datetime.datetime.now()
    # Set target time for today at 21:00:00
    scheduled_time = now.replace(hour=21, minute=0, second=0, microsecond=0)

    # If it's already past 21:00 today, schedule for tomorrow
    if now > scheduled_time:
        print("It's past 21:00 today, scheduling for tomorrow.")
        scheduled_time += datetime.timedelta(days=1)

    wait_seconds = (scheduled_time - now).total_seconds()

    print(f"✅ Script initialized. Waiting until {scheduled_time.strftime('%Y-%m-%d %H:%M:%S')} to start.")
    print(f"(Press Ctrl+C to cancel)")

    try:
        time.sleep(wait_seconds)
    except KeyboardInterrupt:
        print("\nScript cancelled by user during wait period. Exiting.")
        return

    print("\n🚀 It's time! Starting execution loop...")

    # --- REPEATING (SPAM) LOGIC ---
    try:
        while True:
            success = perform_trade_attempt()
            if success:
                print("\n🎉 Trade was successful. Script is now stopping.")
                break  # Exit the loop on success

            print("--- Attempt failed. Retrying in 0.5 seconds... ---")
            time.sleep(0.5)  # Pause briefly to avoid overwhelming the server

    except KeyboardInterrupt:
        print("\nScript stopped by user (Ctrl+C). Exiting.")


if __name__ == "__main__":
    main()









