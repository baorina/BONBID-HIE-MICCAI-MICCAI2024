# Copyright 2023 Radboud University Medical Center
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
from pathlib import Path
import glob
from gcapi import Client
import gcapi
import os.path as osp
import os

savepath="./Track2/"

#  Install gcapi client and retrieve api token as described here:
#  https://grand-challenge.org/documentation/what-can-gc-api-be-used-for/#install-gcapi

mytoken="966d61f867a7cc9b66bba05e4d3a50b6b5b876aa91cc21bbaf2b8d21ca1430ba"

def get_prediction_outputs(predictions_file,team_n):
    token = mytoken # Replace with your own token. Keep this token private!
    client = gcapi.Client(token=token)

    with open(predictions_file) as f:
        prediction_data = json.load(f)

    def download_image(pk, filename):
        details = client.images.detail(pk=pk)
        client.images.download(url=details["api_url"], filename=filename)

    def download_json(pk, filename):
        details = client.files.detail(pk=pk)
        client.files.download(url=details["api_url"], filename=filename)


    #os.mkdir(osp.join(savepath,team_n))

    # iterate through all the outputs of each job.
    for job in prediction_data:
        outputs = job["outputs"]
        for output in outputs:
            if output["value"] is not None:
                # if the output is an image, download the image
                # we use the job pk as folder, so all outputs of one job end up in the same folder
                # you can change this if needed
                if "Zmap" in job["inputs"][1]["image"]["name"]:
                    filename=Path(job["inputs"][0]["image"]["name"].split("-ADC")[0]+"_pred")
                else:
                    filename=Path(job["inputs"][1]["image"]["name"].split("-ADC")[0]+"_pred")
                #print(filename)
                print ("rina check!!!!",filename)

                savename=osp.join(savepath,team_n,filename)
                print (savename)
                download_json(
                    pk=output["interface"]["pk"],filename=savename)

if __name__ == "__main__":

    # for team_n in ["civalab","xleratorxlerator9","frimpz","schlauglab",
    # "rajroy","IWM","imad.toubal","UNeImage","ngzvh","ashwin_dhakal","civa",
    # "arda.aydn","punithakumar","tiansong_philips"]:
    #for team_n in ["piaozhehao5"]:

    for team_n in ["downtoyou","xleratorxlerator9","rongxux","djc0105","intMain"]:
            #try:
            # assumes a folder named predictions with all the prediction files
            #predictions_folder = Path.cwd() / "predictions"
            #predictions_folder = "./"

            #prediction_files = [f for f in predictions_folder.glob("*.json") if f.is_file()]
            #prediction_files=[team_n+"/predictions.json"]
            #for prediction_file in prediction_files:
            prediction_file="./Teams/"+team_n+"/predictions.json"
            print (prediction_file)
            get_prediction_outputs(prediction_file,team_n)
            #except Exception as ex:
            #print("Wrong")