import requests
import json


class MakeApiCall:

    def get_data(self, api):
        response = requests.get(f"{api}")
        if response.status_code == 200:
            self.formatted_print(response.json())
            # print(response)
            print("sucessfully fetched the data")
        else:
            print(
                f"Hello person, there's a {response.status_code} error with your request")

    def formatted_print(self, obj):
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)

    
if __name__ == "__main__":
    api_call = MakeApiCall()
    api_call.get_data("https://af63-103-169-159-101.in.ngrok.io/api/files")