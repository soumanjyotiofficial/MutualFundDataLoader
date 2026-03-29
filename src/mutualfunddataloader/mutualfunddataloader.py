import requests as req
from time import sleep
import datetime as dt


class MutualFundDataLoader:
    def __init__(self):
        self.base_url = "https://api.mfapi.in" #Based URL
        self.mf = self.base_url + "/mf" #Endpoint to get all mutual fund list
        

    def get_all_mf_list(self):
        """
        Get a list of all mutual funds available in the API.
        :return: A list of mutual funds or an error message
        """
        try:
            url = self.mf
            response = req.get(url).json()
            return response # Return the JSON response as a Python object
        except req.exceptions.RequestException as e:
            return [{"error": str(e)}]  # Return an error message if the request fails
        

    def get_historical_nav(self, mf_code, start_date, end_date:dt.datetime):
        """
        Get historical NAV data for a specific mutual fund code.
        :param mf_code: The mutual fund code (e.g., "110022")
        :return: A list of historical NAV data or an error message
        """
        try:
            url = self.mf + f"/{mf_code}?startDate={str(start_date)}&endDate={str(end_date)}"
            response = req.get(url).json()
            if response.get('status')=="SUCCESS":
                return response
            return response

        except req.exceptions.RequestException as e:
            return [{"error": str(e)}] 
    

    def mf_eligible_for_historical(self):
        """
        Check if a mutual fund is eligible for SIP (Systematic Investment Plan).
        :param mf_code: The mutual fund code (e.g., "110022")
        :return: A boolean indicating SIP eligibility or an error message
        """
        try:
            mflist = [a for a in self.get_all_mf_list() if a.get('isinGrowth')!=None and a.get('isinDivReinvestment')!=None]
            return mflist
        except req.exceptions.RequestException as e:
            return {"error": "Hello"}


    def searh_mutualfund(self, name):
        url = f"{self.mf}/search?q={name}"
        try:
            response = req.get(url).json()
            return response
        except req.exceptions.RequestException as e:
            return {"error": str(e)}
        
    def get_latest_nav(self, mf_code):
        url = f"{self.mf}/{mf_code}/latest"
        try:
            response = req.get(url).json()
            if response.get('status')=="SUCCESS":
                return response # Return the latest NAV data
            return response
        except req.exceptions.RequestException as e:
            return {"error": str(e)}


