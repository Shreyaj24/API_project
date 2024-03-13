import requests
from postcode_dto import Postcode
from terminated_postcode import TerminatedPostcode

class PostcodeFinder():

    def _open_postcode_json_link(self, postcode):
        try:
            json_res_postcode = requests.get(f"https://api.postcodes.io/postcodes/{postcode}").json()
            if json_res_postcode["status"] == 200 or json_res_postcode["status"] == 201:
                result_dict = json_res_postcode["result"]
                pc_obj = Postcode(result_dict["postcode"],result_dict["admin_district"], result_dict["country"],result_dict["region"], result_dict["eastings"], result_dict["northings"])
                return pc_obj
            else:
                print(f'Unexpected error occurred: {json_res_postcode["status"]}')
                return None
        except requests.exceptions.HTTPError as e:
            print("HTTP Error: ",e)



    def _get_terminated_postcode(self, postcode):
        try:
            json_ter_postcode = requests.get(f"https://api.postcodes.io/terminated_postcodes/{postcode}").json()
            if json_ter_postcode["status"] == 200:
                result_ter_dict = json_ter_postcode["result"]
                ter_pc_obj = TerminatedPostcode(result_ter_dict["postcode"], result_ter_dict["year_terminated"], result_ter_dict["month_terminated"])
                return ter_pc_obj
            else:
                print(f'Unexpected error occurred: {json_ter_postcode["status"]}')
                return None
        except requests.exceptions.HTTPError as e:
            print("HTTP Error: ",e)

    def _post_request_postcode(self, postcode_list):
        postcode_dict = {}
        postcode_dict["postcodes"] = postcode_list
        try:
            post_data_res = requests.post("https://api.postcodes.io/postcodes", json = postcode_dict, headers={"Content-Type": "application/json"}).json()
            if post_data_res["status"] == 200:
                result_post_list = post_data_res["result"]
                post_address_list = []
                for each_dict in result_post_list:
                    post_address_obj = Postcode(each_dict["result"]["postcode"],each_dict["result"]["admin_district"], each_dict["result"]["country"],each_dict["result"]["region"], each_dict["result"]["eastings"], each_dict["result"]["northings"])
                    post_address_list.append(post_address_obj)
                return post_address_list
            else:
                print(f'Unexpected error occurred: {post_data_res["status"]}')
                return None
        except requests.exceptions.HTTPError as e:
            print("HTTP Error: ", e)

postcode_obj = PostcodeFinder()

print(postcode_obj._open_postcode_json_link("LE96TQ"))

print(postcode_obj._get_terminated_postcode("E1W1UU"))

postcode_list = ["PR3 0SG", "M45 6GN", "EX165BL"]
print(postcode_obj._post_request_postcode(postcode_list))

