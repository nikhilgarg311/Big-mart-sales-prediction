{"metadata":{"kernelspec":{"language":"python","display_name":"Python 3","name":"python3"},"language_info":{"pygments_lexer":"ipython3","nbconvert_exporter":"python","version":"3.6.4","file_extension":".py","codemirror_mode":{"name":"ipython","version":3},"name":"python","mimetype":"text/x-python"}},"nbformat_minor":4,"nbformat":4,"cells":[{"cell_type":"code","source":"# %% [markdown]\n# # Importing Libraries\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false}}\n\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false}}\n\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:15.468554Z\",\"iopub.execute_input\":\"2021-11-17T17:27:15.468980Z\",\"iopub.status.idle\":\"2021-11-17T17:27:17.834751Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:15.468894Z\",\"shell.execute_reply\":\"2021-11-17T17:27:17.833805Z\"}}\nimport pandas as pd\nimport numpy as np\nimport matplotlib.pyplot as plt\nimport seaborn as sns\nfrom scipy import stats\n\n#for Spliting Data and Hyperparameter Tuning \nfrom sklearn.model_selection import train_test_split,GridSearchCV\n\n#Importing Machine Learning Model\nfrom catboost import CatBoostRegressor\n#from ngboost import NGBRegressor\nfrom sklearn import ensemble\nfrom sklearn.linear_model import LinearRegression\nfrom xgboost import XGBRFRegressor\nfrom sklearn.tree import DecisionTreeRegressor\nfrom sklearn.neighbors import KNeighborsRegressor\nfrom sklearn.neural_network import MLPRegressor\nfrom sklearn.svm import SVR\nfrom lightgbm import LGBMRegressor\n\n#statistical Tools\nfrom sklearn import metrics\n\n# %% [markdown]\n# # Reading CSV Files\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:17.836408Z\",\"iopub.execute_input\":\"2021-11-17T17:27:17.836701Z\",\"iopub.status.idle\":\"2021-11-17T17:27:17.900331Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:17.836666Z\",\"shell.execute_reply\":\"2021-11-17T17:27:17.899401Z\"}}\ntest=pd.read_csv(\"../input/bigmart/test.csv\")\ntrain=pd.read_csv(\"../input/bigmart/train.csv\")\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:17.901820Z\",\"iopub.execute_input\":\"2021-11-17T17:27:17.902092Z\",\"iopub.status.idle\":\"2021-11-17T17:27:17.929670Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:17.902067Z\",\"shell.execute_reply\":\"2021-11-17T17:27:17.928954Z\"}}\ntest.head()\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:17.930874Z\",\"iopub.execute_input\":\"2021-11-17T17:27:17.931243Z\",\"iopub.status.idle\":\"2021-11-17T17:27:17.949678Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:17.931217Z\",\"shell.execute_reply\":\"2021-11-17T17:27:17.949014Z\"}}\ntrain.head()\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:17.950601Z\",\"iopub.execute_input\":\"2021-11-17T17:27:17.950991Z\",\"iopub.status.idle\":\"2021-11-17T17:27:17.971416Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:17.950961Z\",\"shell.execute_reply\":\"2021-11-17T17:27:17.970796Z\"}}\ntrain.info()\n\n# %% [markdown]\n# # Removing columns with alot of null values\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:17.972265Z\",\"iopub.execute_input\":\"2021-11-17T17:27:17.972613Z\",\"iopub.status.idle\":\"2021-11-17T17:27:17.976447Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:17.972586Z\",\"shell.execute_reply\":\"2021-11-17T17:27:17.975464Z\"}}\nimport seaborn as sns\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:17.977584Z\",\"iopub.execute_input\":\"2021-11-17T17:27:17.977864Z\",\"iopub.status.idle\":\"2021-11-17T17:27:18.520449Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:17.977838Z\",\"shell.execute_reply\":\"2021-11-17T17:27:18.519370Z\"}}\nsns.heatmap(train.isnull())\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:18.523890Z\",\"iopub.execute_input\":\"2021-11-17T17:27:18.524553Z\",\"iopub.status.idle\":\"2021-11-17T17:27:18.529337Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:18.524508Z\",\"shell.execute_reply\":\"2021-11-17T17:27:18.528482Z\"}}\ndf=pd.DataFrame(train)\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:18.530907Z\",\"iopub.execute_input\":\"2021-11-17T17:27:18.531158Z\",\"iopub.status.idle\":\"2021-11-17T17:27:18.544018Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:18.531135Z\",\"shell.execute_reply\":\"2021-11-17T17:27:18.542992Z\"}}\ndf.drop(\"Outlet_Size\",axis=1,inplace=True)\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:18.545401Z\",\"iopub.execute_input\":\"2021-11-17T17:27:18.545827Z\",\"iopub.status.idle\":\"2021-11-17T17:27:18.553674Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:18.545794Z\",\"shell.execute_reply\":\"2021-11-17T17:27:18.553018Z\"}}\ndf.drop(\"Item_Weight\",axis=1,inplace=True)\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false}}\n\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:18.554867Z\",\"iopub.execute_input\":\"2021-11-17T17:27:18.555406Z\",\"iopub.status.idle\":\"2021-11-17T17:27:18.575795Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:18.555366Z\",\"shell.execute_reply\":\"2021-11-17T17:27:18.574797Z\"}}\ndf.head()\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:18.577208Z\",\"iopub.execute_input\":\"2021-11-17T17:27:18.577543Z\",\"iopub.status.idle\":\"2021-11-17T17:27:18.580906Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:18.577513Z\",\"shell.execute_reply\":\"2021-11-17T17:27:18.579993Z\"}}\n#sns.heatmap(df.isnull())\n\n# %% [markdown]\n# # Exploring  each variable\n\n# %% [markdown]\n# * Variable--   Description\n# * Item_Identifier--  Unique product ID\n# * Item_Weight-- Weight of product\n# * Item_Fat_Content--  Whether the product is low fat or not\n# * Item_Visibility--  The % of total display area of all products in a store allocated to the particular product\n# * Item_Type--  The category to which the product belongs\n# * Item_MRP--  Maximum Retail Price (list price) of the product\n# * Outlet_Identifier--  Unique store ID\n# * Outlet_Establishment_Year--  The year in which store was established\n# * Outlet_Size--  The size of the store in terms of ground area covered\n# * Outlet_Location_Type--  The type of city in which the store is located\n# * Outlet_Type--  Whether the outlet is just a grocery store or some sort of supermarket\n# *  Item_Outlet_Sales--  Sales of the product in the particular store. This is the outcome variable to be predicted.\n\n# %% [markdown]\n# product id does not matter us i.e the column named Item_Identifier is not of use right now.\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:18.582185Z\",\"iopub.execute_input\":\"2021-11-17T17:27:18.582682Z\",\"iopub.status.idle\":\"2021-11-17T17:27:18.593711Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:18.582643Z\",\"shell.execute_reply\":\"2021-11-17T17:27:18.592763Z\"}}\ndf.drop(\"Item_Identifier\",inplace=True,axis=1)\n\n# %% [markdown]\n# item weight dropped out earlier\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:18.594857Z\",\"iopub.execute_input\":\"2021-11-17T17:27:18.595302Z\",\"iopub.status.idle\":\"2021-11-17T17:27:18.608250Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:18.595270Z\",\"shell.execute_reply\":\"2021-11-17T17:27:18.607525Z\"}}\nprint(len(np.unique(df[\"Item_Fat_Content\"])))\n\n# %% [markdown]\n# \n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:18.609486Z\",\"iopub.execute_input\":\"2021-11-17T17:27:18.609948Z\",\"iopub.status.idle\":\"2021-11-17T17:27:18.750635Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:18.609918Z\",\"shell.execute_reply\":\"2021-11-17T17:27:18.749669Z\"}}\nplt.figure(figsize=(10,5))\nplt.hist(x=\"Item_Fat_Content\",bins=10,data=df)\nplt.yticks(size = 20)\nplt.xticks(size = 13)\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:18.752090Z\",\"iopub.execute_input\":\"2021-11-17T17:27:18.752461Z\",\"iopub.status.idle\":\"2021-11-17T17:27:18.761239Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:18.752418Z\",\"shell.execute_reply\":\"2021-11-17T17:27:18.760223Z\"}}\nfat={\"Low Fat\":0,\"Regular\":1,\"low fat\":0,\"LF\":0,\"reg\":1}\ndf.Item_Fat_Content=[fat[item]for item in df.Item_Fat_Content]\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:18.762804Z\",\"iopub.execute_input\":\"2021-11-17T17:27:18.763179Z\",\"iopub.status.idle\":\"2021-11-17T17:27:18.926790Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:18.763141Z\",\"shell.execute_reply\":\"2021-11-17T17:27:18.925829Z\"}}\nplt.figure(figsize=(10,5))\nplt.hist(x=\"Item_Fat_Content\",bins=10,data=df)\nplt.yticks(size = 20)\nplt.xticks(size = 13)\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:18.928098Z\",\"iopub.execute_input\":\"2021-11-17T17:27:18.928383Z\",\"iopub.status.idle\":\"2021-11-17T17:27:19.122258Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:18.928354Z\",\"shell.execute_reply\":\"2021-11-17T17:27:19.120838Z\"}}\nplt.figure(figsize=(30,10))\nplt.hist(x=\"Item_Visibility\",bins=10,data=df)\nplt.yticks(size = 20)\nplt.xticks(size = 20)\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:19.123679Z\",\"iopub.execute_input\":\"2021-11-17T17:27:19.124251Z\",\"iopub.status.idle\":\"2021-11-17T17:27:19.135693Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:19.124196Z\",\"shell.execute_reply\":\"2021-11-17T17:27:19.134697Z\"}}\nnp.unique(df[\"Item_Type\"])\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:19.137259Z\",\"iopub.execute_input\":\"2021-11-17T17:27:19.137692Z\",\"iopub.status.idle\":\"2021-11-17T17:27:19.153376Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:19.137650Z\",\"shell.execute_reply\":\"2021-11-17T17:27:19.152377Z\"}}\ntemp=df.groupby('Item_Type',as_index=False)['Item_Visibility'].mean()\ntemp\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:19.154871Z\",\"iopub.execute_input\":\"2021-11-17T17:27:19.155254Z\",\"iopub.status.idle\":\"2021-11-17T17:27:19.165661Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:19.155206Z\",\"shell.execute_reply\":\"2021-11-17T17:27:19.164673Z\"}}\nitemtype={'Baking Goods':0, 'Breads':1, 'Breakfast':2, 'Canned':3, 'Dairy':4,\n       'Frozen Foods':5, 'Fruits and Vegetables':6, 'Hard Drinks':7,\n       'Health and Hygiene':12, 'Household':11, 'Meat':10, 'Others':9, 'Seafood':8,\n       'Snack Foods':13, 'Soft Drinks':14, 'Starchy Foods':15}\ndf.Item_Type=[itemtype[item] for item in df.Item_Type]\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:19.166947Z\",\"iopub.execute_input\":\"2021-11-17T17:27:19.167523Z\",\"iopub.status.idle\":\"2021-11-17T17:27:19.177451Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:19.167481Z\",\"shell.execute_reply\":\"2021-11-17T17:27:19.176814Z\"}}\ndf.drop(\"Outlet_Identifier\",axis=1,inplace=True)\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:19.181183Z\",\"iopub.execute_input\":\"2021-11-17T17:27:19.181657Z\",\"iopub.status.idle\":\"2021-11-17T17:27:19.198928Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:19.181625Z\",\"shell.execute_reply\":\"2021-11-17T17:27:19.198050Z\"}}\ndf.head()\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:19.202044Z\",\"iopub.execute_input\":\"2021-11-17T17:27:19.202659Z\",\"iopub.status.idle\":\"2021-11-17T17:27:19.211685Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:19.202616Z\",\"shell.execute_reply\":\"2021-11-17T17:27:19.210979Z\"}}\ndf[\"Age_Outlet\"]=2021-df[\"Outlet_Establishment_Year\"]\ndf.drop(\"Outlet_Establishment_Year\",axis=1,inplace=True)\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:19.213179Z\",\"iopub.execute_input\":\"2021-11-17T17:27:19.213853Z\",\"iopub.status.idle\":\"2021-11-17T17:27:19.223623Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:19.213811Z\",\"shell.execute_reply\":\"2021-11-17T17:27:19.222836Z\"}}\nprint(len(np.unique(df[\"Item_Type\"])))\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:19.224983Z\",\"iopub.execute_input\":\"2021-11-17T17:27:19.225605Z\",\"iopub.status.idle\":\"2021-11-17T17:27:19.477792Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:19.225564Z\",\"shell.execute_reply\":\"2021-11-17T17:27:19.475475Z\"}}\nplt.figure(figsize=(30,10))\nplt.hist(x=\"Item_Type\",bins=40,data=df)\nplt.yticks(size = 20)\nplt.xticks(size = 13)\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:19.479238Z\",\"iopub.execute_input\":\"2021-11-17T17:27:19.479606Z\",\"iopub.status.idle\":\"2021-11-17T17:27:19.490264Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:19.479567Z\",\"shell.execute_reply\":\"2021-11-17T17:27:19.489383Z\"}}\nnp.unique(df[\"Outlet_Type\"])\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:19.491470Z\",\"iopub.execute_input\":\"2021-11-17T17:27:19.491756Z\",\"iopub.status.idle\":\"2021-11-17T17:27:19.671278Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:19.491730Z\",\"shell.execute_reply\":\"2021-11-17T17:27:19.670415Z\"}}\nplt.figure(figsize=(30,10))\nplt.hist(x=\"Outlet_Type\",data=df)\nplt.yticks(size = 20)\nplt.xticks(size = 20)\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:19.672547Z\",\"iopub.execute_input\":\"2021-11-17T17:27:19.672828Z\",\"iopub.status.idle\":\"2021-11-17T17:27:19.687256Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:19.672801Z\",\"shell.execute_reply\":\"2021-11-17T17:27:19.686176Z\"}}\ndf.head()\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:19.688446Z\",\"iopub.execute_input\":\"2021-11-17T17:27:19.688698Z\",\"iopub.status.idle\":\"2021-11-17T17:27:19.702595Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:19.688673Z\",\"shell.execute_reply\":\"2021-11-17T17:27:19.701714Z\"}}\nnp.unique(df.Outlet_Location_Type)\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:19.704022Z\",\"iopub.execute_input\":\"2021-11-17T17:27:19.704631Z\",\"iopub.status.idle\":\"2021-11-17T17:27:19.717496Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:19.704589Z\",\"shell.execute_reply\":\"2021-11-17T17:27:19.716815Z\"}}\ntier={'Tier 1':0, 'Tier 2':1, 'Tier 3':2}\ndf.Outlet_Location_Type=[tier[item] for item in df.Outlet_Location_Type]\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:19.718608Z\",\"iopub.execute_input\":\"2021-11-17T17:27:19.719067Z\",\"iopub.status.idle\":\"2021-11-17T17:27:19.733625Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:19.719036Z\",\"shell.execute_reply\":\"2021-11-17T17:27:19.732791Z\"}}\nmarket_type={'Grocery Store':0, 'Supermarket Type1':1, 'Supermarket Type2':2,\n       'Supermarket Type3':3}\ndf.Outlet_Type=[market_type[item] for item in df.Outlet_Type]\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:19.734652Z\",\"iopub.execute_input\":\"2021-11-17T17:27:19.735065Z\",\"iopub.status.idle\":\"2021-11-17T17:27:19.835702Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:19.735039Z\",\"shell.execute_reply\":\"2021-11-17T17:27:19.835072Z\"}}\nplt.boxplot(df[\"Item_MRP\"])\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:19.836624Z\",\"iopub.execute_input\":\"2021-11-17T17:27:19.836997Z\",\"iopub.status.idle\":\"2021-11-17T17:27:19.938418Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:19.836970Z\",\"shell.execute_reply\":\"2021-11-17T17:27:19.937621Z\"}}\nplt.boxplot(df[\"Item_Visibility\"])\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:19.939517Z\",\"iopub.execute_input\":\"2021-11-17T17:27:19.939810Z\",\"iopub.status.idle\":\"2021-11-17T17:27:19.949346Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:19.939784Z\",\"shell.execute_reply\":\"2021-11-17T17:27:19.948554Z\"}}\ndf[\"Item_Visibility\"].describe()\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:19.950597Z\",\"iopub.execute_input\":\"2021-11-17T17:27:19.951264Z\",\"iopub.status.idle\":\"2021-11-17T17:27:19.958919Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:19.951224Z\",\"shell.execute_reply\":\"2021-11-17T17:27:19.958108Z\"}}\ndf[\"Item_Visibility\"].median()\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:19.960157Z\",\"iopub.execute_input\":\"2021-11-17T17:27:19.960678Z\",\"iopub.status.idle\":\"2021-11-17T17:27:19.969037Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:19.960639Z\",\"shell.execute_reply\":\"2021-11-17T17:27:19.968044Z\"}}\nq3,q1=np.percentile(df[\"Item_Visibility\"],[75,25])\niqr=q3-q1\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:19.970168Z\",\"iopub.execute_input\":\"2021-11-17T17:27:19.970692Z\",\"iopub.status.idle\":\"2021-11-17T17:27:20.623046Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:19.970662Z\",\"shell.execute_reply\":\"2021-11-17T17:27:20.622068Z\"}}\nfor i in range(len(df)):\n    if df.loc[i,\"Item_Visibility\"]>1.5*iqr:\n        df.loc[i,\"Item_Visibility\"]=0.066132\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:20.624429Z\",\"iopub.execute_input\":\"2021-11-17T17:27:20.624831Z\",\"iopub.status.idle\":\"2021-11-17T17:27:20.721970Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:20.624787Z\",\"shell.execute_reply\":\"2021-11-17T17:27:20.721084Z\"}}\nplt.boxplot(df[\"Item_Visibility\"])\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:20.723263Z\",\"iopub.execute_input\":\"2021-11-17T17:27:20.723536Z\",\"iopub.status.idle\":\"2021-11-17T17:27:20.727264Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:20.723511Z\",\"shell.execute_reply\":\"2021-11-17T17:27:20.726306Z\"}}\nfrom sklearn.linear_model import LinearRegression\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:20.728120Z\",\"iopub.execute_input\":\"2021-11-17T17:27:20.728581Z\",\"iopub.status.idle\":\"2021-11-17T17:27:20.739452Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:20.728553Z\",\"shell.execute_reply\":\"2021-11-17T17:27:20.738684Z\"}}\nlinear_reg=LinearRegression()\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false}}\n\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:20.740412Z\",\"iopub.execute_input\":\"2021-11-17T17:27:20.740819Z\",\"iopub.status.idle\":\"2021-11-17T17:27:20.751324Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:20.740789Z\",\"shell.execute_reply\":\"2021-11-17T17:27:20.750629Z\"}}\nfrom sklearn.ensemble import RandomForestRegressor\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:20.752502Z\",\"iopub.execute_input\":\"2021-11-17T17:27:20.752948Z\",\"iopub.status.idle\":\"2021-11-17T17:27:20.764450Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:20.752919Z\",\"shell.execute_reply\":\"2021-11-17T17:27:20.763634Z\"}}\nrf=RandomForestRegressor()\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:20.765415Z\",\"iopub.execute_input\":\"2021-11-17T17:27:20.765839Z\",\"iopub.status.idle\":\"2021-11-17T17:27:20.776043Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:20.765810Z\",\"shell.execute_reply\":\"2021-11-17T17:27:20.775259Z\"}}\nfrom sklearn.model_selection import RandomizedSearchCV\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:20.776990Z\",\"iopub.execute_input\":\"2021-11-17T17:27:20.777353Z\",\"iopub.status.idle\":\"2021-11-17T17:27:20.788005Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:20.777326Z\",\"shell.execute_reply\":\"2021-11-17T17:27:20.787185Z\"}}\nn_estimators=[int(x) for x in np.linspace(start = 100, stop = 1200, num = 12)]\nmax_depth=[int(x) for x in np.linspace(5, 30, num = 6)]\nmax_features=['auto','sqrt']\nmin_samples_split=[2,5,10,15,25,35,50]\nmin_samples_leaf=[1,2,5,10]\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:20.788965Z\",\"iopub.execute_input\":\"2021-11-17T17:27:20.789320Z\",\"iopub.status.idle\":\"2021-11-17T17:27:20.800673Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:20.789295Z\",\"shell.execute_reply\":\"2021-11-17T17:27:20.800008Z\"}}\nprint(n_estimators)\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:20.801636Z\",\"iopub.execute_input\":\"2021-11-17T17:27:20.802058Z\",\"iopub.status.idle\":\"2021-11-17T17:27:20.816939Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:20.802028Z\",\"shell.execute_reply\":\"2021-11-17T17:27:20.815953Z\"}}\nparams={'n_estimators':n_estimators,\n       \n       'max_depth':max_depth,\n        'max_features':max_features,\n       'min_samples_split':min_samples_split,\n       'min_samples_leaf':min_samples_leaf}\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:20.818232Z\",\"iopub.execute_input\":\"2021-11-17T17:27:20.818686Z\",\"iopub.status.idle\":\"2021-11-17T17:27:20.831358Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:20.818654Z\",\"shell.execute_reply\":\"2021-11-17T17:27:20.830582Z\"}}\ndf.dtypes\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:20.832665Z\",\"iopub.execute_input\":\"2021-11-17T17:27:20.833170Z\",\"iopub.status.idle\":\"2021-11-17T17:27:20.840064Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:20.833138Z\",\"shell.execute_reply\":\"2021-11-17T17:27:20.839161Z\"}}\nrf_ran=RandomizedSearchCV(estimator=rf,param_distributions=params,random_state=101,scoring='neg_mean_squared_error',cv=5,n_jobs=1,return_train_score=True,verbose=2,n_iter=10)\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:20.841436Z\",\"iopub.execute_input\":\"2021-11-17T17:27:20.842037Z\",\"iopub.status.idle\":\"2021-11-17T17:27:20.854791Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:20.841995Z\",\"shell.execute_reply\":\"2021-11-17T17:27:20.854016Z\"}}\nx_train,x_test,y_train,y_test=train_test_split(df.drop(\"Item_Outlet_Sales\",axis=1),df[\"Item_Outlet_Sales\"],test_size=0.8,random_state=42)\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:20.855914Z\",\"iopub.execute_input\":\"2021-11-17T17:27:20.856455Z\",\"iopub.status.idle\":\"2021-11-17T17:27:20.864566Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:20.856415Z\",\"shell.execute_reply\":\"2021-11-17T17:27:20.863842Z\"}}\n#rf_ran.fit(x_train,y_train)\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:20.865815Z\",\"iopub.execute_input\":\"2021-11-17T17:27:20.866412Z\",\"iopub.status.idle\":\"2021-11-17T17:27:20.874283Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:20.866347Z\",\"shell.execute_reply\":\"2021-11-17T17:27:20.873617Z\"}}\n#rf_ran.best_params_\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:20.875547Z\",\"iopub.execute_input\":\"2021-11-17T17:27:20.876095Z\",\"iopub.status.idle\":\"2021-11-17T17:27:20.884453Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:20.876054Z\",\"shell.execute_reply\":\"2021-11-17T17:27:20.883554Z\"}}\n#model=RandomForestRegressor(n_estimators=400,min_samples_split=50,min_samples_leaf= 1,max_features= 'auto',max_depth=5)\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:20.885657Z\",\"iopub.execute_input\":\"2021-11-17T17:27:20.886232Z\",\"iopub.status.idle\":\"2021-11-17T17:27:20.894085Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:20.886189Z\",\"shell.execute_reply\":\"2021-11-17T17:27:20.893388Z\"}}\n#model.fit(x_train,y_train)\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:20.895169Z\",\"iopub.execute_input\":\"2021-11-17T17:27:20.895758Z\",\"iopub.status.idle\":\"2021-11-17T17:27:20.905066Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:20.895688Z\",\"shell.execute_reply\":\"2021-11-17T17:27:20.904047Z\"}}\n#preds=model.predict(x_test)\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:20.906424Z\",\"iopub.execute_input\":\"2021-11-17T17:27:20.907031Z\",\"iopub.status.idle\":\"2021-11-17T17:27:20.914860Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:20.906985Z\",\"shell.execute_reply\":\"2021-11-17T17:27:20.914128Z\"}}\n#sns.distplot(preds-y_test)\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:20.916281Z\",\"iopub.execute_input\":\"2021-11-17T17:27:20.916639Z\",\"iopub.status.idle\":\"2021-11-17T17:27:20.923977Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:20.916610Z\",\"shell.execute_reply\":\"2021-11-17T17:27:20.923201Z\"}}\n#plt.scatter(preds,y_test)\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:20.925570Z\",\"iopub.execute_input\":\"2021-11-17T17:27:20.926160Z\",\"iopub.status.idle\":\"2021-11-17T17:27:20.933480Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:20.926119Z\",\"shell.execute_reply\":\"2021-11-17T17:27:20.932812Z\"}}\n#from sklearn import metrics\n#print('MAE:', metrics.mean_absolute_error(y_test, preds))\n#print('MSE:', metrics.mean_squared_error(y_test, preds))\n#print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, preds)))\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:20.934460Z\",\"iopub.execute_input\":\"2021-11-17T17:27:20.934890Z\",\"iopub.status.idle\":\"2021-11-17T17:27:20.946472Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:20.934860Z\",\"shell.execute_reply\":\"2021-11-17T17:27:20.945713Z\"}}\n#reg=LinearRegression()\n#model1=reg.fit(x_train,y_train)\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:20.949124Z\",\"iopub.execute_input\":\"2021-11-17T17:27:20.949557Z\",\"iopub.status.idle\":\"2021-11-17T17:27:20.959326Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:20.949528Z\",\"shell.execute_reply\":\"2021-11-17T17:27:20.958561Z\"}}\n#preds2=model1.predict(x_test)\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:20.960383Z\",\"iopub.execute_input\":\"2021-11-17T17:27:20.960780Z\",\"iopub.status.idle\":\"2021-11-17T17:27:20.970777Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:20.960745Z\",\"shell.execute_reply\":\"2021-11-17T17:27:20.970050Z\"}}\n#sns.distplot(preds2-y_test)\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:20.971824Z\",\"iopub.execute_input\":\"2021-11-17T17:27:20.972193Z\",\"iopub.status.idle\":\"2021-11-17T17:27:20.981896Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:20.972165Z\",\"shell.execute_reply\":\"2021-11-17T17:27:20.981035Z\"}}\n#plt.scatter(preds2,y_test)\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:20.983045Z\",\"iopub.execute_input\":\"2021-11-17T17:27:20.983466Z\",\"iopub.status.idle\":\"2021-11-17T17:27:20.991740Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:20.983437Z\",\"shell.execute_reply\":\"2021-11-17T17:27:20.990906Z\"}}\n#from sklearn import metrics\n#print('MAE:', metrics.mean_absolute_error(y_test, preds2))\n#print('MSE:', metrics.mean_squared_error(y_test, preds2))\n#print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, preds2)))\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:20.992779Z\",\"iopub.execute_input\":\"2021-11-17T17:27:20.993162Z\",\"iopub.status.idle\":\"2021-11-17T17:27:21.007460Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:20.993124Z\",\"shell.execute_reply\":\"2021-11-17T17:27:21.006744Z\"}}\nlr = LinearRegression()\nrfc = ensemble.RandomForestRegressor(n_estimators=400, bootstrap=True, min_samples_leaf=100, min_samples_split=8, max_depth=6)\nada = ensemble.AdaBoostRegressor(n_estimators=1000, learning_rate=0.01)\ngbr = ensemble.GradientBoostingRegressor(learning_rate=0.01, n_estimators=1000, max_depth=5, min_samples_split=8, min_samples_leaf=100)\nxgb = XGBRFRegressor(n_jobs=-1, n_estimators=1000, max_depth=5)\ncat = CatBoostRegressor(verbose=0)\ndtr = DecisionTreeRegressor(max_depth=15, min_samples_leaf=100)\nlgbr = LGBMRegressor(n_estimators = 440, learning_rate=0.01, max_depth=12, objective='tweedie', num_leaves=15, num_threads = 4)\n#ngb = NGBRegressor(minibatch_frac=0.5, col_sample=0.5, Base=dtr)\nknn = KNeighborsRegressor()\n\nmlp = MLPRegressor()\n\nsvr = SVR(kernel='linear', C=10, gamma='scale')\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:21.008428Z\",\"iopub.execute_input\":\"2021-11-17T17:27:21.008847Z\",\"iopub.status.idle\":\"2021-11-17T17:27:21.022690Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:21.008818Z\",\"shell.execute_reply\":\"2021-11-17T17:27:21.021843Z\"}}\naccuracy = {}\nrmse = {}\nexplained_variance = {}\nmax_error = {}\nMAE = {}\n\ndef train_model(model, model_name):\n    print(model_name)\n    model.fit(x_train,y_train)\n    pred = model.predict(x_test)\n\n    acc = metrics.r2_score(y_test, pred)*100\n    accuracy[model_name] = acc\n    print('R2_Score',acc)\n\n    met = np.sqrt(metrics.mean_squared_error(y_test, pred))\n    print('RMSE : ', met)\n    rmse[model_name] = met\n\n    var = (metrics.explained_variance_score(y_test, pred))\n    print('Explained_Variance : ', var)\n    explained_variance[model_name] = var\n\n    error = (metrics.max_error(y_test, pred))\n    print('Max_Error : ', error)\n    max_error[model_name] = error\n    \n    err = metrics.mean_absolute_error(y_test, pred)\n    print(\"Mean Absolute Error\", err)\n    MAE[model_name] = err\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:21.023691Z\",\"iopub.execute_input\":\"2021-11-17T17:27:21.024131Z\",\"iopub.status.idle\":\"2021-11-17T17:27:21.980665Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:21.024101Z\",\"shell.execute_reply\":\"2021-11-17T17:27:21.979675Z\"}}\ntrain_model(rfc, \"Random Forest Regression\")\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:21.981909Z\",\"iopub.execute_input\":\"2021-11-17T17:27:21.982172Z\",\"iopub.status.idle\":\"2021-11-17T17:27:22.343526Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:21.982145Z\",\"shell.execute_reply\":\"2021-11-17T17:27:22.342544Z\"}}\ntrain_model(lgbr, \"LightGBM Regression\")\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:22.347957Z\",\"iopub.execute_input\":\"2021-11-17T17:27:22.348450Z\",\"iopub.status.idle\":\"2021-11-17T17:27:22.361586Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:22.348416Z\",\"shell.execute_reply\":\"2021-11-17T17:27:22.360916Z\"}}\ntrain_model(dtr, \"Decision Tree Regression\")\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:22.362815Z\",\"iopub.execute_input\":\"2021-11-17T17:27:22.363324Z\",\"iopub.status.idle\":\"2021-11-17T17:27:23.507983Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:22.363294Z\",\"shell.execute_reply\":\"2021-11-17T17:27:23.506855Z\"}}\ntrain_model(cat, \"Cat boost Regression\")\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:23.509174Z\",\"iopub.execute_input\":\"2021-11-17T17:27:23.509440Z\",\"iopub.status.idle\":\"2021-11-17T17:27:24.667596Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:23.509414Z\",\"shell.execute_reply\":\"2021-11-17T17:27:24.666591Z\"}}\ntrain_model(xgb, \"XGB Regression\")\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:24.669238Z\",\"iopub.execute_input\":\"2021-11-17T17:27:24.669639Z\",\"iopub.status.idle\":\"2021-11-17T17:27:26.775449Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:24.669597Z\",\"shell.execute_reply\":\"2021-11-17T17:27:26.774414Z\"}}\ntrain_model(mlp, \"mlp\")\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:26.777250Z\",\"iopub.execute_input\":\"2021-11-17T17:27:26.778029Z\",\"iopub.status.idle\":\"2021-11-17T17:27:29.180827Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:26.777973Z\",\"shell.execute_reply\":\"2021-11-17T17:27:29.180016Z\"}}\ntrain_model(gbr, \"gbr\")\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:27:29.181865Z\",\"iopub.execute_input\":\"2021-11-17T17:27:29.182264Z\",\"iopub.status.idle\":\"2021-11-17T17:27:32.936093Z\",\"shell.execute_reply.started\":\"2021-11-17T17:27:29.182224Z\",\"shell.execute_reply\":\"2021-11-17T17:27:32.935084Z\"}}\ntrain_model(ada, \"ada\")\n\n# %% [code] {\"execution\":{\"iopub.status.busy\":\"2021-11-17T17:40:47.332602Z\",\"iopub.execute_input\":\"2021-11-17T17:40:47.332981Z\",\"iopub.status.idle\":\"2021-11-17T17:40:47.476822Z\",\"shell.execute_reply.started\":\"2021-11-17T17:40:47.332948Z\",\"shell.execute_reply\":\"2021-11-17T17:40:47.475827Z\"}}\nimport pickle\n# open a file, where you ant to store the data\nfile = open('model.pkl', 'wb')\n\n# dump information to that file\npickle.dump(xgb, file)","metadata":{"_uuid":"bd99b9ff-f5ca-400a-9809-262a336bd4b3","_cell_guid":"6bcb87b8-7924-499d-bad3-03e6fd02a373","collapsed":false,"jupyter":{"outputs_hidden":false},"trusted":true},"execution_count":null,"outputs":[]}]}