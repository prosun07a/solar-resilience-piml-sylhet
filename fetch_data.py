import requests
import pandas as pd
import os

# --- LOGIC: Configuration Constants ---
# We define these at the top so the 'Experiment' is easily repeatable 
# for other cities (like Dhaka or Chittagong) later.
LAT = 24.8949
LON = 91.8687
START_DATE = "20150101" # Format: YYYYMMDD
END_DATE = "20241231"   # 10 years of data for high-variance training

def fetch_sylhet_solar_data():
    print(f"--- Initiating Data Fetch for Sylhet ({LAT}, {LON}) ---")
    
    # --- LOGIC: The API Request ---
    # We use NASA's POWER API because it provides 'Analysis-Ready' data.
    # We request 'DAILY' frequency to balance detail with computational speed.
    url = (
        f"https://power.larc.nasa.gov/api/temporal/daily/point?"
        f"parameters=ALLSKY_SFC_SW_DWN,T2M,RH2M&"
        f"community=RE&longitude={LON}&latitude={LAT}&"
        f"start={START_DATE}&end={END_DATE}&format=JSON"
    )
    
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status() # LOGIC: Stop immediately if the server fails
        data = response.json()
        
        # --- LOGIC: Data Transformation ---
        # NASA returns a complex JSON. We need a 'Flat Table' (DataFrame) 
        # so our Machine Learning model can read it row-by-row.
        features = data['properties']['parameter']
        df = pd.DataFrame(features)
        
        # Save to our 'raw' directory (The 'Lab Vault')
        output_path = "data/raw/sylhet_solar_raw.csv"
        df.to_csv(output_path)
        
        print(f"SUCCESS: Dataset saved to {output_path}")
        print(f"Total Days Captured: {len(df)}")
        
    except Exception as e:
        print(f"FAILURE: Research interrupted by error: {e}")

if __name__ == "__main__":
    fetch_sylhet_solar_data()