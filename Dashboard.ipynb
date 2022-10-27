{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "[DIY Covid-19 Dashboard Kit](https://github.com/fsmeraldi/diy-covid19dash) (C) Fabrizio Smeraldi, 2020 ([f.smeraldi@qmul.ac.uk](mailto:f.smeraldi@qmul.ac.uk) - [web](http://www.eecs.qmul.ac.uk/~fabri/)). All rights reserved."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# DIY Covid-19 Dashboard"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This is a template for your DIY Covid Dashboard, to which you can add the code you developed in the previous notebooks. The dashboard will be displayed using [voila](https://voila.readthedocs.io/en/stable/index.html), a Python dashboarding tool that converts notebooks to standalone dashboards. Contrary to the other libraries we have seen, the ```voila``` package must be installed using *pip* or *conda* but it does not need to be imported - it rather acts at the level of the notebook server. Package ```voila``` is already installed on the EECS JupyterHub as well as in the binder - to install it locally, follow the [instructions](https://voila.readthedocs.io/en/stable/install.html) online.\n",
    "\n",
    "Broadly speaking, Voila acts by **running all the cells in your notebook** when the dashboard is first loaded; it then hides all code cells and displays all markdown cells and any outputs, including widgets. However, the code is still there in the background and handles any interaction with the widgets. To view this dashboard template rendered in Voila click [here](https://mybinder.org/v2/gh/fsmeraldi/diy-covid19dash/main?urlpath=%2Fvoila%2Frender%2FDashboard.ipynb)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from IPython.display import clear_output\n",
    "import ipywidgets as wdg\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import json\n",
    "from uk_covid19 import Cov19API"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "%matplotlib inline\n",
    "# make figures larger\n",
    "plt.rcParams['figure.dpi'] = 100"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Load initial data from disk\n",
    "\n",
    "You should include \"canned\" data in ```.json``` files along with your dashboard. When the dashboard starts, it should load that data (the code below will be hidden when the dashboard is rendered by Voila)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Load JSON files and store the raw data in some variable. Edit as appropriate\n",
    "with open(\"admissions_with_covidOccupiedMVBeds.json\", \"rt\") as INFILE:\n",
    "    jsondata=json.load(INFILE)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Wrangle the data\n",
    "\n",
    "The dashboard should contain the logic to wrangle the raw data into a ```DataFrame``` (or more than one, as required) that will be used for plotting. The wrangling code should be put into a function and called on the data from the JSON file (we'll need to call it again on any data downloaded from the API).  In this template, we just pretend we are wrangling ```rawdata``` and generate a dataframe with some random data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>admissions</th>\n",
       "      <th>occupied ventilator beds</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2020-03-01</th>\n",
       "      <td>3.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-03-02</th>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-03-03</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-03-04</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-03-05</th>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2022-10-15</th>\n",
       "      <td>900.0</td>\n",
       "      <td>221.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2022-10-16</th>\n",
       "      <td>1206.0</td>\n",
       "      <td>217.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2022-10-17</th>\n",
       "      <td>1121.0</td>\n",
       "      <td>207.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2022-10-18</th>\n",
       "      <td>0.0</td>\n",
       "      <td>200.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2022-10-19</th>\n",
       "      <td>0.0</td>\n",
       "      <td>206.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>963 rows × 2 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "           admissions occupied ventilator beds\n",
       "2020-03-01        3.0                      0.0\n",
       "2020-03-02        1.0                      0.0\n",
       "2020-03-03        0.0                      0.0\n",
       "2020-03-04        0.0                      0.0\n",
       "2020-03-05        1.0                      0.0\n",
       "...               ...                      ...\n",
       "2022-10-15      900.0                    221.0\n",
       "2022-10-16     1206.0                    217.0\n",
       "2022-10-17     1121.0                    207.0\n",
       "2022-10-18        0.0                    200.0\n",
       "2022-10-19        0.0                    206.0\n",
       "\n",
       "[963 rows x 2 columns]"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def parse_date(datestring):\n",
    "    \"\"\" Convert a date string into a pandas datetime object \"\"\"\n",
    "    return pd.to_datetime(datestring, format=\"%Y-%m-%d\")\n",
    "\n",
    "def wrangle_data(rawdata):\n",
    "    \"\"\" Parameters: rawdata - data from json file or API call. Returns a dataframe.\n",
    "    Edit to include the code that wrangles the data, creates the dataframe and fills it in. \"\"\"\n",
    "    datalist=rawdata['data']\n",
    "    dates=[dictionary['date'] for dictionary in datalist ]\n",
    "    dates.sort()\n",
    "    startdate=parse_date(dates[0])\n",
    "    enddate=parse_date(dates[-1])\n",
    "    index=pd.date_range(startdate, enddate, freq='D')\n",
    "    df=pd.DataFrame(index=index, columns=['admissions', 'occupied ventilator beds'])\n",
    "    for entry in datalist: # each entry is a dictionary with date, cases, hospital and deaths\n",
    "        date=parse_date(entry['date'])\n",
    "        for column in ['admissions', 'occupied ventilator beds']:\n",
    "            # check that nothing is there yet - just in case some dates are duplicated,\n",
    "            # maybe with data for different columns in each entry\n",
    "            if pd.isna(df.loc[date, column]): \n",
    "                # replace None with 0 in our data \n",
    "                value= float(entry[column]) if entry[column]!=None else 0.0\n",
    "                # this is the way you access a specific location in the dataframe - use .loc\n",
    "                # and put index,column in a single set of [ ]\n",
    "                df.loc[date, column]=value\n",
    "\n",
    "    # fill in any remaining \"holes\" due to missing dates\n",
    "    df.fillna(0.0, inplace=True)\n",
    "    return df\n",
    "# putting the wrangling code into a function allows you to call it again after refreshing the data through \n",
    "# the API. You should call the function directly on the JSON data when the dashboard starts, by including \n",
    "# the call in the cell as below:\n",
    "df=wrangle_data(jsondata) # df is the dataframe for plotting\n",
    "df"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Download current data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Give your users an option to refresh the dataset - a \"refresh\" button will do. The button callback should\n",
    "* call the code that accesses the API and download some fresh raw data;\n",
    "* wrangle that data into a dataframe and update the corresponding (global) variable for plotting;\n",
    "* optionally: force a redraw of the graph and give the user some fredback.\n",
    "\n",
    "Once you get it to work, you may want to wrap your API call inside an exception handler, so that the user is informed, the \"canned\" data are not overwritten and nothing crashes if for any reason the server cannot be reached or data are not available.\n",
    "\n",
    "After you refresh the data, graphs will not update until the user interacts with a widget. You can trick ```iPywidgets``` into redrawing the graph by simulating interaction, as in the ```refresh_graph``` function we define in the Graph and Analysis section below.\n",
    "\n",
    "Clicking on the button below just generates some more random data and refreshes the graph. The button should read *Fetch Data*. If you see anything else, take a deep breath :)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Place your API access code in this function. Do not call this function directly; it will be called by \n",
    "# the button callback. \n",
    "def access_api():\n",
    "    \"\"\" Accesses the PHE API. Returns raw data in the same format as data loaded from the \"canned\" JSON file. \"\"\"\n",
    "    # put code for polling the API here\n",
    "    filters = [\n",
    "    'areaType=nation'  \n",
    "    ]\n",
    "    structure = {\n",
    "        \"date\": \"date\",\n",
    "        \"admissions\": \"newAdmissions\",\n",
    "        \"occupied ventilator beds\": \"covidOccupiedMVBeds\"\n",
    "\n",
    "    }\n",
    "    api = Cov19API(filters=filters, structure=structure)\n",
    "    jsondata=api.get_json()\n",
    "    return jsondata "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "a6a82c6689b3418b9147bda5361656f7",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Button(button_style='info', description='Fetch Data', icon='download', style=ButtonStyle(), tooltip='Click to …"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Printout from this function will be lost in Voila unless captured in an\n",
    "# output widget - therefore, we give feedback to the user by changing the \n",
    "# appearance of the button\n",
    "def api_button_callback(button):\n",
    "    \"\"\" Button callback - it must take the button as its parameter (unused in this case).\n",
    "    Accesses API, wrangles data, updates global variable df used for plotting. \"\"\"\n",
    "    # Get fresh data from the API. If you have time, include some error handling\n",
    "    # around this call.\n",
    "    apidata=access_api()\n",
    "    # wrangle the data and overwrite the dataframe for plotting\n",
    "    global df\n",
    "    df=wrangle_data(apidata)\n",
    "    # the graph won't refresh until the user interacts with the widget.\n",
    "    # this function simulates the interaction, see Graph and Analysis below.\n",
    "    # you can omit this step in the first instance\n",
    "    refresh_graph()\n",
    "    # after all is done, you can switch the icon on the button to a \"check\" sign\n",
    "    # and optionally disable the button - it won't be needed again. You can use icons\n",
    "    # \"unlink\" or \"times\" and change the button text to \"Unavailable\" in case the \n",
    "    # api call fails.\n",
    "    apibutton.icon=\"check\"\n",
    "    # apibutton.disabled=True\n",
    "\n",
    "    \n",
    "apibutton=wdg.Button(\n",
    "    description='Fetch Data', # you may want to change this...\n",
    "    disabled=False,\n",
    "    button_style='info', # 'success', 'info', 'warning', 'danger' or ''\n",
    "    tooltip=\"Click to download current Public Health England data\",\n",
    "    # FontAwesome names without the `fa-` prefix - try \"download\"\n",
    "    icon='download'\n",
    ")\n",
    "\n",
    "# remember to register your button callback function with the button\n",
    "apibutton.on_click(api_button_callback) # the name of your function inside these brackets\n",
    "\n",
    "display(apibutton)\n",
    "\n",
    "# run all cells before clicking on this button"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Graphs and Analysis"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Include at least one graph with interactive controls, as well as some instructions for the user and/or comments on what the graph represents and how it should be explored (this example shows two random walks)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "c537b9a841e84a6f81046cc5dd35da36",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(SelectMultiple(description='Stats:', index=(0, 1), options=('admissions', 'occupied ventilator …"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "7f06727b539f4462a1a1089179af9773",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Output()"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "series=wdg.SelectMultiple(\n",
    "    options=['admissions', 'occupied ventilator beds'],\n",
    "    value=['admissions', 'occupied ventilator beds'],\n",
    "    rows=2,\n",
    "    description='Stats:',\n",
    "    disabled=False\n",
    ")\n",
    "\n",
    "scale=wdg.RadioButtons(\n",
    "    options=['linear', 'log'],\n",
    "#    value='pineapple', # Defaults to 'pineapple'\n",
    "#    layout={'width': 'max-content'}, # If the items' names are long\n",
    "    description='Scale:',\n",
    "    disabled=False\n",
    ")\n",
    "\n",
    "# try replacing HBox with a VBox\n",
    "controls=wdg.HBox([series, scale])\n",
    "\n",
    "def timeseries_graph(gcols, gscale):\n",
    "    if gscale=='linear':\n",
    "        logscale=False\n",
    "    else:\n",
    "        logscale=True\n",
    "    ncols=len(gcols)\n",
    "    if ncols>0:\n",
    "        df[list(gcols)].plot(logy=logscale)\n",
    "        plt.show() # important - graphs won't update if this is missing \n",
    "    else:\n",
    "        print(\"Click to select data for graph\")\n",
    "        print(\"(CTRL-Click to select more than one category)\")\n",
    "\n",
    "# keep calling timeseries_graph(gcols=value_of_series, gscale=value_of_scale); \n",
    "# capture output in widget graph   \n",
    "graph=wdg.interactive_output(timeseries_graph, {'gcols': series, 'gscale': scale})\n",
    "\n",
    "display(controls, graph)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Deploying the dashboard\n",
    "\n",
    "Once your code is ready and you are satisfied with the appearance of the graphs, replace all the text boxes above with the explanations you would like a dashboard user to see. The next step is deploying the dashboard online - there are several [options](https://voila.readthedocs.io/en/stable/deploy.html) for this, we suggest deploying as a [Binder](https://mybinder.org/). This is basically the same technique that has been used to package this tutorial and to deploy this template dashboard. The instructions may seem a bit involved, but the actual steps are surprisingly easy - we will be going through them together during a live session. You will need an account on [GitHub](https://github.com/) for this - if you don't have one already, now it's the time to create it. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Author and Copyright Notice** Remember if you deploy this dashboard as a Binder it will be publicly accessible. Take credit for your work! Also acknowledge the data source: *Based on UK Government [data](https://coronavirus.data.gov.uk/) published by [Public Health England](https://www.gov.uk/government/organisations/public-health-england).*"
   ]
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
   "version": "3.10.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
