{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Capstone 2: Biodiversity Project"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Introduction\n",
    "You are a biodiversity analyst working for the National Parks Service.  You're going to help them analyze some data about species at various national parks.\n",
    "\n",
    "Note: The data that you'll be working with for this project is *inspired* by real data, but is mostly fictional."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Step 1\n",
    "Import the modules that you'll be using in this assignment:\n",
    "- `from matplotlib import pyplot as plt`\n",
    "- `import pandas as pd`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 575,
   "metadata": {},
   "outputs": [],
   "source": [
    "from matplotlib import pyplot as plt\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Step 2\n",
    "You have been given two CSV files. `species_info.csv` with data about different species in our National Parks, including:\n",
    "- The scientific name of each species\n",
    "- The common names of each species\n",
    "- The species conservation status\n",
    "\n",
    "Load the dataset and inspect it:\n",
    "- Load `species_info.csv` into a DataFrame called `species`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 576,
   "metadata": {},
   "outputs": [],
   "source": [
    "species = pd.read_csv('species_info.csv')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Inspect each DataFrame using `.head()`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 577,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  category                scientific_name  \\\n",
      "0   Mammal  Clethrionomys gapperi gapperi   \n",
      "1   Mammal                      Bos bison   \n",
      "2   Mammal                     Bos taurus   \n",
      "3   Mammal                     Ovis aries   \n",
      "4   Mammal                 Cervus elaphus   \n",
      "\n",
      "                                        common_names conservation_status  \n",
      "0                           Gapper's Red-Backed Vole                 NaN  \n",
      "1                              American Bison, Bison                 NaN  \n",
      "2  Aurochs, Aurochs, Domestic Cattle (Feral), Dom...                 NaN  \n",
      "3  Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)                 NaN  \n",
      "4                                      Wapiti Or Elk                 NaN  \n"
     ]
    }
   ],
   "source": [
    "print species.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Step 3\n",
    "Let's start by learning a bit more about our data.  Answer each of the following questions."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "How many different species are in the `species` DataFrame?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 578,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5541 Unique species\n",
      "5504 Unique common names\n"
     ]
    }
   ],
   "source": [
    "numUnqSpecies = species.scientific_name.nunique()\n",
    "numSpecies = species.scientific_name.count()\n",
    "\n",
    "numUnqNames = species.common_names.nunique()\n",
    "numNames = species.common_names.count()\n",
    "print (str(numUnqSpecies) + ' Unique species')\n",
    "print (str(numUnqNames) + ' Unique common names')\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What are the different values of `category` in `species`?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 579,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Mammal' 'Bird' 'Reptile' 'Amphibian' 'Fish' 'Vascular Plant'\n",
      " 'Nonvascular Plant']\n"
     ]
    }
   ],
   "source": [
    "types_of_bio = species.category.unique()\n",
    "print types_of_bio"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What are the different values of `conservation_status`?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 580,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[nan 'Species of Concern' 'Endangered' 'Threatened' 'In Recovery']\n"
     ]
    }
   ],
   "source": [
    "status = species.conservation_status.unique()\n",
    "print status"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Step 4\n",
    "Let's start doing some analysis!\n",
    "\n",
    "The column `conservation_status` has several possible values:\n",
    "- `Species of Concern`: declining or appear to be in need of conservation\n",
    "- `Threatened`: vulnerable to endangerment in the near future\n",
    "- `Endangered`: seriously at risk of extinction\n",
    "- `In Recovery`: formerly `Endangered`, but currnetly neither in danger of extinction throughout all or a significant portion of its range\n",
    "\n",
    "We'd like to count up how many species meet each of these criteria.  Use `groupby` to count how many `scientific_name` meet each of these criteria."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 581,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "conservation_status\n",
      "Endangered             15\n",
      "In Recovery             4\n",
      "Species of Concern    151\n",
      "Threatened             10\n",
      "Name: scientific_name, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "status_count = species.groupby('conservation_status').scientific_name.nunique()\n",
    "print status_count"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As we saw before, there are far more than 200 species in the `species` table.  Clearly, only a small number of them are categorized as needing some sort of protection.  The rest have `conservation_status` equal to `None`.  Because `groupby` does not include `None`, we will need to fill in the null values.  We can do this using `.fillna`.  We pass in however we want to fill in our `None` values as an argument.\n",
    "\n",
    "Paste the following code and run it to see replace `None` with `No Intervention`:\n",
    "```python\n",
    "species.fillna('No Intervention', inplace=True)\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 582,
   "metadata": {},
   "outputs": [],
   "source": [
    "species.fillna('No Intervention', inplace=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Great! Now run the same `groupby` as before to see how many species require `No Protection`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 583,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "conservation_status\n",
      "Endangered              15\n",
      "In Recovery              4\n",
      "No Intervention       5363\n",
      "Species of Concern     151\n",
      "Threatened              10\n",
      "Name: scientific_name, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "status_count = species.groupby('conservation_status').scientific_name.nunique()\n",
    "print status_count"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's use `plt.bar` to create a bar chart.  First, let's sort the columns by how many species are in each categories.  We can do this using `.sort_values`.  We use the the keyword `by` to indicate which column we want to sort by.\n",
    "\n",
    "Paste the following code and run it to create a new DataFrame called `protection_counts`, which is sorted by `scientific_name`:\n",
    "```python\n",
    "protection_counts = species.groupby('conservation_status')\\\n",
    "    .scientific_name.count().reset_index()\\\n",
    "    .sort_values(by='scientific_name')\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 584,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<bound method DataFrame.head of   conservation_status  scientific_name\n",
      "1         In Recovery                4\n",
      "4          Threatened               10\n",
      "0          Endangered               16\n",
      "3  Species of Concern              161\n",
      "2     No Intervention             5633>\n",
      "  conservation_status  scientific_name\n",
      "1         In Recovery                4\n",
      "4          Threatened               10\n",
      "0          Endangered               16\n",
      "3  Species of Concern              161\n"
     ]
    }
   ],
   "source": [
    "protection_counts = species.groupby('conservation_status')\\\n",
    "    .scientific_name.count().reset_index().sort_values(by='scientific_name')\n",
    "    \n",
    "print protection_counts.head\n",
    "\n",
    "endangered_counts = protection_counts.iloc[0:4].sort_values(by='scientific_name')\n",
    "print endangered_counts"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now let's create a bar chart!\n",
    "1. Start by creating a wide figure with `figsize=(10, 4)`\n",
    "1. Start by creating an axes object called `ax` using `plt.subplot`.\n",
    "2. Create a bar chart whose heights are equal to `scientific_name` column of `protection_counts`.\n",
    "3. Create an x-tick for each of the bars.\n",
    "4. Label each x-tick with the label from `conservation_status` in `protection_counts`\n",
    "5. Label the y-axis `Number of Species`\n",
    "6. Title the graph `Conservation Status by Species`\n",
    "7. Plot the grap using `plt.show()`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 585,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 720x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 576x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(10,4))\n",
    "ax=plt.subplot()\n",
    "barlistLarge = plt.bar(protection_counts.conservation_status, protection_counts.scientific_name, color='orchid')\n",
    "ax.set_ylabel('Number of Species', size='14')\n",
    "ax.set_title('Conservation Status by Species', size='20')\n",
    "barlistLarge[0].set_color('darkorchid')\n",
    "barlistLarge[1].set_color('plum')\n",
    "barlistLarge[2].set_color('thistle')\n",
    "barlistLarge[3].set_color('mediumorchid')\n",
    "barlistLarge[4].set_color('darkviolet')\n",
    "plt.show()\n",
    "\n",
    "plt.figure(figsize=(8,4))\n",
    "ax1=plt.subplot()\n",
    "barlist = plt.bar(endangered_counts.conservation_status, endangered_counts.scientific_name)\n",
    "ax1.set_ylabel('Number of Species', size='14')\n",
    "ax1.set_title('Conservation Status by Species', size='20')\n",
    "\n",
    "barlist[0].set_color('darkorchid')\n",
    "barlist[1].set_color('plum')\n",
    "barlist[2].set_color('thistle')\n",
    "barlist[3].set_color('mediumorchid')\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Step 4\n",
    "Are certain types of species more likely to be endangered?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's create a new column in `species` called `is_protected`, which is `True` if `conservation_status` is not equal to `No Intervention`, and `False` otherwise."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 586,
   "metadata": {},
   "outputs": [],
   "source": [
    "species['is_protected'] = species.conservation_status.apply(lambda x:True if x!='No Intervention' else False)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's group by *both* `category` and `is_protected`.  Save your results to `category_counts`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 587,
   "metadata": {},
   "outputs": [],
   "source": [
    "category_counts = species.groupby(['category','is_protected']).scientific_name.count().reset_index()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Examine `category_count` using `head()`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 588,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    category  is_protected  scientific_name\n",
      "0  Amphibian         False               73\n",
      "1  Amphibian          True                7\n",
      "2       Bird         False              442\n",
      "3       Bird          True               79\n",
      "4       Fish         False              116\n"
     ]
    }
   ],
   "source": [
    "print category_counts.head(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It's going to be easier to view this data if we pivot it.  Using `pivot`, rearange `category_counts` so that:\n",
    "- `columns` is `conservation_status`\n",
    "- `index` is `category`\n",
    "- `values` is `scientific_name`\n",
    "\n",
    "Save your pivoted data to `category_pivot`. Remember to `reset_index()` at the end."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 589,
   "metadata": {},
   "outputs": [],
   "source": [
    "category_pivot = category_counts.pivot(columns='is_protected',index='category', values='scientific_name').reset_index()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Examine `category_pivot`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 590,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "is_protected           category  False  True\n",
      "0                     Amphibian     73     7\n",
      "1                          Bird    442    79\n",
      "2                          Fish    116    11\n",
      "3                        Mammal    176    38\n",
      "4             Nonvascular Plant    328     5\n",
      "5                       Reptile     74     5\n",
      "6                Vascular Plant   4424    46\n"
     ]
    }
   ],
   "source": [
    "print category_pivot"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Use the `.columns` property to  rename the categories `True` and `False` to something more description:\n",
    "- Leave `category` as `category`\n",
    "- Rename `False` to `not_protected`\n",
    "- Rename `True` to `protected`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 591,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "            category  not_protected  protected\n",
      "0          Amphibian             73          7\n",
      "1               Bird            442         79\n",
      "2               Fish            116         11\n",
      "3             Mammal            176         38\n",
      "4  Nonvascular Plant            328          5\n",
      "5            Reptile             74          5\n",
      "6     Vascular Plant           4424         46\n"
     ]
    }
   ],
   "source": [
    "category_pivot.columns = ['category','not_protected','protected']\n",
    "print category_pivot"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's create a new column of `category_pivot` called `percent_protected`, which is equal to `protected` (the number of species that are protected) divided by `protected` plus `not_protected` (the total number of species)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 592,
   "metadata": {},
   "outputs": [],
   "source": [
    "category_pivot['percent_protected'] = category_pivot['protected']\\\n",
    "            /(category_pivot['protected']+category_pivot['not_protected'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Examine `category_pivot`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 593,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "            category  not_protected  protected  percent_protected\n",
      "0          Amphibian             73          7           0.087500\n",
      "1               Bird            442         79           0.151631\n",
      "2               Fish            116         11           0.086614\n",
      "3             Mammal            176         38           0.177570\n",
      "4  Nonvascular Plant            328          5           0.015015\n",
      "5            Reptile             74          5           0.063291\n",
      "6     Vascular Plant           4424         46           0.010291\n"
     ]
    }
   ],
   "source": [
    "print category_pivot"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It looks like species in category `Mammal` are more likely to be endangered than species in `Bird`.  We're going to do a significance test to see if this statement is true.  Before you do the significance test, consider the following questions:\n",
    "- Is the data numerical or categorical?\n",
    "- How many pieces of data are you comparing?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Based on those answers, you should choose to do a *chi squared test*.  In order to run a chi squared test, we'll need to create a contingency table.  Our contingency table should look like this:\n",
    "\n",
    "||protected|not protected|\n",
    "|-|-|-|\n",
    "|Mammal|?|?|\n",
    "|Bird|?|?|\n",
    "\n",
    "Create a table called `contingency` and fill it in with the correct numbers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 594,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[38, 176], [79, 442]]\n"
     ]
    }
   ],
   "source": [
    "contingency = [[38,176],[79,442]]\n",
    "print contingency"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In order to perform our chi square test, we'll need to import the correct function from scipy.  Past the following code and run it:\n",
    "```py\n",
    "from scipy.stats import chi2_contingency\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 595,
   "metadata": {},
   "outputs": [],
   "source": [
    "from scipy.stats import chi2_contingency"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now run `chi2_contingency` with `contingency`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 596,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.445901703047197\n"
     ]
    }
   ],
   "source": [
    "chi2, pval, dof, expected = chi2_contingency(contingency)\n",
    "print pval"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It looks like this difference isn't significant!\n",
    "\n",
    "Let's test another.  Is the difference between `Reptile` and `Mammal` significant?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 597,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.02338465214871547\n"
     ]
    }
   ],
   "source": [
    "contingency2 = [[38,176],[5,74]]\n",
    "chi2, pval2, dof, expected = chi2_contingency(contingency2)\n",
    "print pval2\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Yes! It looks like there is a significant difference between `Reptile` and `Mammal`!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Step 5"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Conservationists have been recording sightings of different species at several national parks for the past 7 days.  They've saved sent you their observations in a file called `observations.csv`.  Load `observations.csv` into a variable called `observations`, then use `head` to view the data."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 598,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "            scientific_name                            park_name  observations\n",
      "0        Vicia benghalensis  Great Smoky Mountains National Park            68\n",
      "1            Neovison vison  Great Smoky Mountains National Park            77\n",
      "2         Prunus subcordata               Yosemite National Park           138\n",
      "3      Abutilon theophrasti                  Bryce National Park            84\n",
      "4  Githopsis specularioides  Great Smoky Mountains National Park            85\n",
      "23296\n"
     ]
    }
   ],
   "source": [
    "observations = pd.read_csv('observations.csv')\n",
    "print observations.head(5)\n",
    "\n",
    "things_seen = observations.scientific_name.count()\n",
    "print things_seen"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Some scientists are studying the number of sheep sightings at different national parks.  There are several different scientific names for different types of sheep.  We'd like to know which rows of `species` are referring to sheep.  Notice that the following code will tell us whether or not a word occurs in a string:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 599,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 599,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Does \"Sheep\" occur in this string?\n",
    "str1 = 'This string contains Sheep'\n",
    "'Sheep' in str1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 600,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 600,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Does \"Sheep\" occur in this string?\n",
    "str2 = 'This string contains Cows'\n",
    "'Sheep' in str2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Use `apply` and a `lambda` function to create a new column in `species` called `is_sheep` which is `True` if the `common_names` contains `'Sheep'`, and `False` otherwise."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 601,
   "metadata": {},
   "outputs": [],
   "source": [
    "species['is_sheep']= species.common_names.apply\\\n",
    "   (lambda x: True if 'Sheep' in x else False)\n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Select the rows of `species` where `is_sheep` is `True` and examine the results."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 602,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "            category              scientific_name  \\\n",
      "3             Mammal                   Ovis aries   \n",
      "1139  Vascular Plant             Rumex acetosella   \n",
      "2233  Vascular Plant           Festuca filiformis   \n",
      "3014          Mammal              Ovis canadensis   \n",
      "3758  Vascular Plant             Rumex acetosella   \n",
      "3761  Vascular Plant            Rumex paucifolius   \n",
      "4091  Vascular Plant                 Carex illota   \n",
      "4383  Vascular Plant  Potentilla ovina var. ovina   \n",
      "4446          Mammal      Ovis canadensis sierrae   \n",
      "\n",
      "                                           common_names conservation_status  \\\n",
      "3     Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)     No Intervention   \n",
      "1139                        Sheep Sorrel, Sheep Sorrell     No Intervention   \n",
      "2233                              Fineleaf Sheep Fescue     No Intervention   \n",
      "3014                       Bighorn Sheep, Bighorn Sheep  Species of Concern   \n",
      "3758  Common Sheep Sorrel, Field Sorrel, Red Sorrel,...     No Intervention   \n",
      "3761   Alpine Sheep Sorrel, Fewleaved Dock, Meadow Dock     No Intervention   \n",
      "4091                       Sheep Sedge, Smallhead Sedge     No Intervention   \n",
      "4383                                   Sheep Cinquefoil     No Intervention   \n",
      "4446                        Sierra Nevada Bighorn Sheep          Endangered   \n",
      "\n",
      "      is_protected  is_sheep  \n",
      "3            False      True  \n",
      "1139         False      True  \n",
      "2233         False      True  \n",
      "3014          True      True  \n",
      "3758         False      True  \n",
      "3761         False      True  \n",
      "4091         False      True  \n",
      "4383         False      True  \n",
      "4446          True      True  \n"
     ]
    }
   ],
   "source": [
    "sheep_name = species[(species.is_sheep == True)]\n",
    "print sheep_name"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Many of the results are actually plants.  Select the rows of `species` where `is_sheep` is `True` and `category` is `Mammal`.  Save the results to the variable `sheep_species`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 603,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "     category          scientific_name  \\\n",
      "3      Mammal               Ovis aries   \n",
      "3014   Mammal          Ovis canadensis   \n",
      "4446   Mammal  Ovis canadensis sierrae   \n",
      "\n",
      "                                           common_names conservation_status  \\\n",
      "3     Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)     No Intervention   \n",
      "3014                       Bighorn Sheep, Bighorn Sheep  Species of Concern   \n",
      "4446                        Sierra Nevada Bighorn Sheep          Endangered   \n",
      "\n",
      "      is_protected  is_sheep  \n",
      "3            False      True  \n",
      "3014          True      True  \n",
      "4446          True      True  \n"
     ]
    }
   ],
   "source": [
    "sheep_species = species[(species.is_sheep == True) & (species.category == 'Mammal')]\n",
    "print sheep_species"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now merge `sheep_species` with `observations` to get a DataFrame with observations of sheep.  Save this DataFrame as `sheep_observations`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 604,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   category          scientific_name  \\\n",
      "0    Mammal               Ovis aries   \n",
      "1    Mammal               Ovis aries   \n",
      "2    Mammal               Ovis aries   \n",
      "3    Mammal               Ovis aries   \n",
      "4    Mammal          Ovis canadensis   \n",
      "5    Mammal          Ovis canadensis   \n",
      "6    Mammal          Ovis canadensis   \n",
      "7    Mammal          Ovis canadensis   \n",
      "8    Mammal  Ovis canadensis sierrae   \n",
      "9    Mammal  Ovis canadensis sierrae   \n",
      "10   Mammal  Ovis canadensis sierrae   \n",
      "11   Mammal  Ovis canadensis sierrae   \n",
      "\n",
      "                                         common_names conservation_status  \\\n",
      "0   Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)     No Intervention   \n",
      "1   Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)     No Intervention   \n",
      "2   Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)     No Intervention   \n",
      "3   Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)     No Intervention   \n",
      "4                        Bighorn Sheep, Bighorn Sheep  Species of Concern   \n",
      "5                        Bighorn Sheep, Bighorn Sheep  Species of Concern   \n",
      "6                        Bighorn Sheep, Bighorn Sheep  Species of Concern   \n",
      "7                        Bighorn Sheep, Bighorn Sheep  Species of Concern   \n",
      "8                         Sierra Nevada Bighorn Sheep          Endangered   \n",
      "9                         Sierra Nevada Bighorn Sheep          Endangered   \n",
      "10                        Sierra Nevada Bighorn Sheep          Endangered   \n",
      "11                        Sierra Nevada Bighorn Sheep          Endangered   \n",
      "\n",
      "    is_protected  is_sheep                            park_name  observations  \n",
      "0          False      True               Yosemite National Park           126  \n",
      "1          False      True  Great Smoky Mountains National Park            76  \n",
      "2          False      True                  Bryce National Park           119  \n",
      "3          False      True            Yellowstone National Park           221  \n",
      "4           True      True            Yellowstone National Park           219  \n",
      "5           True      True                  Bryce National Park           109  \n",
      "6           True      True               Yosemite National Park           117  \n",
      "7           True      True  Great Smoky Mountains National Park            48  \n",
      "8           True      True            Yellowstone National Park            67  \n",
      "9           True      True               Yosemite National Park            39  \n",
      "10          True      True                  Bryce National Park            22  \n",
      "11          True      True  Great Smoky Mountains National Park            25  \n"
     ]
    }
   ],
   "source": [
    "sheep_observations = pd.merge(sheep_species, observations, on='scientific_name', how='inner')\n",
    "print sheep_observations"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "How many total sheep observations (across all three species) were made at each national park?  Use `groupby` to get the `sum` of `observations` for each `park_name`.  Save your answer to `obs_by_park`.\n",
    "\n",
    "This is the total number of sheep observed in each park over the past 7 days."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 605,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                             park_name  observations\n",
      "0                  Bryce National Park           250\n",
      "1  Great Smoky Mountains National Park           149\n",
      "2            Yellowstone National Park           507\n",
      "3               Yosemite National Park           282\n"
     ]
    }
   ],
   "source": [
    "obs_by_park = sheep_observations.groupby('park_name').observations.sum().reset_index()\n",
    "print obs_by_park"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Create a bar chart showing the different number of observations per week at each park.\n",
    "\n",
    "1. Start by creating a wide figure with `figsize=(16, 4)`\n",
    "1. Start by creating an axes object called `ax` using `plt.subplot`.\n",
    "2. Create a bar chart whose heights are equal to `observations` column of `obs_by_park`.\n",
    "3. Create an x-tick for each of the bars.\n",
    "4. Label each x-tick with the label from `park_name` in `obs_by_park`\n",
    "5. Label the y-axis `Number of Observations`\n",
    "6. Title the graph `Observations of Sheep per Week`\n",
    "7. Plot the grap using `plt.show()`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 606,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1152x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(16,4))\n",
    "ax=plt.subplot()\n",
    "plt.bar(obs_by_park.park_name, obs_by_park.observations, color='darkorchid')\n",
    "ax.set_ylabel('Number of Observations', size='14')\n",
    "ax.set_title ('Observations of Sheep per Week', size='20')\n",
    "plt.show()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 607,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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7sX7QW02cFVI3Tzz6AaVV8X7gcUBY0/mWOihhx56nMqHOXdC91AQEREROWX8LvpfA7Odc/1OwfYc3pjXpJPdloiI/PxojK6IiIiIiIiUKEp0RUREREREpERRoisiIiIiIiIlisboioiIiIiISIlSoqYXql69uqtXr96ZDkNERERERESKwcqVK3c552oUVq9EJbr16tVjxYoVZzoMERERERERKQZm9k0k9TRGV0REREREREoUJboiIiIiIiJSoijRFRERERERkRKlRI3RDSc7O5utW7dy+PDhMx2KiJwG0dHR1KlThzJlypzpUERERETkDCnxie7WrVupVKkS9erVw8zOdDgiUoycc+zevZutW7dSv379Mx2OiIiIiJwhJb7r8uHDh6lWrZqSXJFfADOjWrVq6sEhIiIi8gtX4hNdQEmuyC+Ivu8iIiIi8otIdEVEREREROSX47SO0TWzTOAH4CiQ45xLMLNfASlAPSAT6OWc+968ZpnHgSuAg0A/59yqk43hKVtzspvI4w+uaaF1oqKiiImJITs7m9KlS9O3b1/uuOMOSpU6vb8zpKenk5WVxRVXXAHA/PnzWbt2LaNHj45o/ZkzZzJlyhTMjGPHjjFp0iR69OhBUlISjzzyCAkJCcUZfkTq1atHixYt+Oc//wnAvHnzeOutt5g1a1ZE6y9atIgePXrQoEEDDh8+zA033MDYsWMj3n9mZiYfffQRN91004mEz6xZs+jatSvnn38+AAMHDmTkyJFceumlJ7Q9EREREZFfojNxM6pk59yuoPejgfecc5PNbLT//h7gt8DF/qMVMN1//tkpX7486enpAOzYsYObbrqJvXv3Mn78+NMaR3p6OitWrAgkuldddRVXXXVVROtu3bqVSZMmsWrVKqpUqcL+/fvZuXNncYZ7wlasWMHnn39OkyZNTmj9yy67jLfeeosDBw4QHx9P9+7dadGiRWB5Tk4OpUuH/+pkZmbyyiuvnFSi27Rp00Ci+7e//e2EtiMicjI2LNpwpkMQicglSZec6RBE5Cx1NnRd7gHM9l/PBq4OKn/ReT4GqppZ7TMR4KlUs2ZNnnvuOZ588kmccxw+fJj+/fsTExNDs2bNWLhwIeAlPFdffTVXXnkl9evX58knn+Sxxx6jWbNmtG7dmu+++w6AL7/8kssvv5wWLVpw2WWXsX79egDmzp1L06ZN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0224bNmydO/eHYAWLVqQmZkJwLJly7jpppsAuOWWW1i6dGlgnZ49exIVFRV4/7vf/Y5y5cpRvXp1ataseVy32KioKN5++23mzZtHw4YNufPOOxk3blxg+bXXXnvc/lNTU3nxxReJj4+nVatW7N69m02bNpGamkpqairNmjWjefPmrF+/nk2bNgFQt25d2rVrB8DNN9+cJ+ZIJScnEx8fz759+wLdwKOiorjuuusAL5muX79+YHxr3759A4l2sI8//pi1a9fSrl074uPjmT17Nt988w0bNmygdu3atGzZEoDKlStTunTBw9kLOhdXX301pUqV4tJLLy1yd+SlS5dy4403EhUVRa1atejYsSNpaWkAJCYmUqdOHUqVKkV8fDyZmZn5xp7fucrdTnDrff369YmPjwfynu/Y2Fj69OnDSy+9VOjxEBERERE5kyL9a/UD4FEzWwokANf75Q2BLcURWEnVpk0bdu3axc6dO/OUhya+wcqUKYOZAV5Cl9+429w6ABUqVMizrFy5coHX+W3DzEhMTCQxMZEuXbrQv3//QLKbu37wus45nnjiCbp165ZnO++88w733nsvgwcPzlOemZmZJ8bQmAG2bNnClVdeCcCQIUPydOfNtXDhQqpXr56nLDo6OpDYF3Qsgznn6NKlC3PmzMlTnpGRcVxcRRW8fvCxDxdbkyZN8h2rXdBnCXdOnXNhY8/vXC1atKjQayW36/K///1vlixZwvz58/nrX//K559/roRXRERERM5KkbboDgeO4CW4Q5xzWX75b4F3iiOwkmr9+vUcPXqUatWq5Slv3749r776KgBr167ls88+K3Rbbdu25R//+AcAL7/8Mu3btz/huLKysli1alXgfXp6OhdddFGB63Tr1o3p06cHukFv3LiRAwcO0K1bN2bOnBkY7/rtt9+yY8cOADZv3syyZcsAmDNnznEx161bl/T0dNLT08MmuZFo1KgRmZmZgfG7f//73+nYsSMAlSpV4ocffgCgdevWfPjhh4F6Bw8eZOPGjTRq1IisrKxAy+kPP/xATk5OnnVDncy56NSpEz/++GOgSzp442wXL15Mhw4dSElJ4ejRo+zcuZMlS5aQmJhY4GcPF3t+5ypSx44dY8uWLSQnJ/PQQw+xZ8+e03IncBERERGRExFRc4xzbitwZZjyO055RMUskumATrXcMbrgtazN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5ZtPcVwiIiIiIiIiJyTS6YUqA08AvQhJcn1RpzIoERERERERkRMV6fRCjwJxwNXAYeAmYBTenZF7F09oIiIiIiIiIkUX6fRCvwVudM59YGZHgZXOuRQz2wYMBuYVW4QiIiIiIiIiRRBpi25V4Bv/9V6gmv96GdD2VAclIiIiIiIicqIiTXS/BBr4r9cBN5iZAdfiTf0jIiIiIiIiclaINNGdBcT6ryfjdVc+AjwM/N+pD0tERERERETkxEQ6vdCUoNfvm1kjIAHY5Jz7rLiCExERERERESmqSKcXinPOrc5978+bq7lzRURERERE5KwTadflT83sMzO728zqFmtEIiIiIiIiIich0kS3EfAaMBD42swWmtkAM6tcfKGJiIiIiIiIFF1Eia5zbqNzbqxzriHQDvgMeAD4n5m9WpwBioiIiIiIiBRFpC26Ac65T5xzI4AewAbgulMelYiIiIiIiMgJKlKia2YNzOwvZrYOWAp8j9edWUREREREROSsEOldl/8A9AFaAWuAF4CXnXPfFmNsIiIiIiIiIkUWUaILjAbmAIM1b66IiIiIiIiczQpNdM2sDPAq8JRz7pviD0lERERERETkxBU6Rtc5lw0MAqz4wxERERERERE5OZHejCoV6FScgYiIiIiIiIicCpGO0X0PeMDMYoGVwIHghc651051YCIiIiIiIiInItJE90n/eUSYZQ6IOjXhiIiIiIiIiJyciBJd51yR5tsVEREREREROVOUwIqIiIiIiEiJElGia55hZva5mR00swZ++Wgz61W8IYqIiIiIiIhELtIW3T8CfwGeI+80Q98Cw091UCIiIiIiIiInKtJEdwhwm3PucSAnqHwV0OSURyUiIiIiIiJygiJNdC8C1oQpzwbKn7pwRERERERERE5OpInuV0DzMOVXAGtPXTgiIiIiIiIiJyfSeXQfAZ40s3Pwxui2MbNbgLuBAcUVnIiIiIiIiEhRRTqP7gtmVhp4ADgH+DvejahGOOdSijE+ERERERERkSKJtEUX59wMYIaZVQdKOed2FF9YIiIiIiIiIicm0nl0S5lZKQDn3C6glJkNNLO2xRqdiIiIiIiISBFFejOqfwO3A5hZRWAF8DCw2MxujWQDZhZtZsvNbLWZfW5m4/3y+mb2iZltMrMUMyvrl5fz33/hL69XxM8mIiIiIiIiv0CRJrotgPf919cC+4CawG3AXRFu40egk3MuDogHLjez1sD/AVOccxcD3wO/9+v/HvjeOfdrYIpfT0RERERERKRAkSa6lYA9/uuuwOvOuWy85Pf/RbIB59nvvy3jPxzQCZjnl88GrvZf9/Df4y/vbGYWYbwiIiIiIiLyCxVporsZaGdmFYBuwLt++a+Ag5HuzMyizCwd2OFv40tgj3Mux6+yFbjAf30BsAXAX74XqBZmm4PMbIWZrdi5c2ekoYiIiIiIiEgJFWmi+xjelEJb8aYVWuKXdwA+i3Rnzrmjzrl4oA6QCDQOV81/Dtd6644rcO4551yCcy6hRo0akYYiIiIiIiIiJVSk8+g+a2YrgbrAu865Y/6iL4H7irpT59weM1sEtAaqmllpv9W2DpDlV9vq72+rP4dvFeC7ou5LREREREREflkibdHFObfCOfd60DhbnHP/ds59GMn6ZlbDzKr6r8sDvwHWAQuB6/1qfYF/+a/n++/xl7/vnDuuRVdEREREREQkWMSJrpldbWZLzGyX//jAzK4pwr5qAwvNLANIw2sZfgu4BxhpZl/gjcF93q//PFDNLx8JjC7CvkREREREROQXKqKuy2b2J+AB4EVgll/cBnjFzO5zzj1S2DaccxlAszDlX+GN1w0tPwz0jCQ+ERERERERkVwRJbp4c+UOd87NCCqbaWbLgQlAoYmuiIiIiIiIyOkQadflinhjaUMt9JeJiIiIiIiInBUibdF9A++GUJNDyq/Du2mUiIiIiIiEsWHRhjMdgkhELkm65EyHcMrkm+ia2cigt18Ao80sGVjml7X2H48VX3giIiIiIiIiRVNQi+7tIe+/Bxr6j+CyfnjjdEVERERERETOuHwTXedc/dMZiIiIiIiIiMipEPE8ugBmVt3MqhVXMCIiIiIiIiInq9BE18wqm9kTZrYL2A7sMLNdZjbNzKoUf4giIiIiIiIikSvwrstmVhX4CLgQeAVYCxhwKfB7oJOZtXPO7S3uQEVEREREREQiUdj0Qn8BHHCxc25b8AIzGwu869cZVTzhiYiIiIiIiBRNYV2XrwVGhSa5AM65LOBuvLl0RURERERERM4KhSW65wMZBSxf7dcREREREREROSsUlujuoeBEto5fR0REREREROSsUFii+z4wpoDl9/p1RERERERERM4Khd2Majyw3MyWA48C6/FuTtUEGAlcAiQWa4QiIiIiIiIiRVBgouuc22BmXYCZwBy8JBe8KYbWAV2cc+uLN8SSZcOiDWc6BJGIXJJ0yZkOQURERETkhBTWootzbjnQ1MzigYZ+8UbnXHqxRiYiIiIiIiJyAgpNdHP5ia2SWxER+f/t3XmUZWV57/Hvz8YoDkGRQWQQTJAARgk2kwyBqCwhRjCRgFcjYgwqKDhclai5kuuEoih4lWtrjOKynQIKGAcQgcZcEAGBZpBRVAQBRVAQBJrn/rHfkpPqc6pOVZ/qqq7+ftaqVee8+z17P6fWeWvvZ7/DkSRJmtOGTnQlSZIkTd1PP37/bIcgDWWL3Wc7gtGZbNVlSZIkSZJWKSa6kiRJkqR5ZWCim+TTSR7bHu+WxGHOkiRJkqQ5b6Ie3ZcCj26PzwTWnvlwJEmSJElaMRP10t4AvC7JaXTfm7tTkl/3q1hVS2YgNkmSJEmSpmyiRI3o2ZYAABZOSURBVPfNwCeBfwYK+OqAegUsGHFc85ar7mlVMZ9W3ZMkSdLqZWCiW1UnAycneRxwO7A1cOvKCkySJEmSpOmYdIGpqrojyR7ANVX1wEqISZIkSZKkaRtqJeWqOjvJI5K8DNiKbrjyFcDiqvr9TAYoSZJWrqu/MtsRSMN57mwHIGnOGup7dJNsBVwNHAPsAOwIfBi4OsmWMxeeJEmSJElTM1SiCxwLXAxsUlW7VtWuwCbAJcBHZio4SZIkSZKmaqihy8DOwHZV9Zuxgqr6TZK3A+fNSGSSJEmSJE3DsD269wKP61O+VtsmSZIkSdKcMGyieyrwySQ7J1nQfnYBPgGcMswOkmyc5MwkVya5PMnhrXztJKcnuab9fnwrT5Ljklyb5NIk207nDUqSJEmSVi/DJrqHA9cA59D14N4LnE23QNXrh9zHA8CbqmpLusWsDm2LXB0BnFFVmwNntOcAewGbt5+DgeOHPI4kSZIkaTU27NcL3QHsk+RPgS2BAFdU1bXDHqiqbgZubo9/m+RKYENgH2D3Vu2zwFnAW1v5CVVVwHlJHpdkg7YfSZIkSZL6GnYxKgBaYjt0cjtIkk2BvwC+D6w/lrxW1c1J1mvVNgR+1vOyG1vZf0t0kxxM1+PLJptssqKhSZIkSZJWccMOXR6ZJI8BTgRe37uKc7+qfcpquYKqRVW1sKoWrrvuuqMKU5IkSZK0ilqpiW6Sh9MluZ+vqpNa8S1JNmjbNwBubeU3Ahv3vHwj4KaVFaskSZIkadW00hLdJAH+Dbiyqo7p2XQKcGB7fCBwck/5y9rqyzsCdzo/V5IkSZI0mUnn6CZZg24O7NeqakV6VHcG/gFYmuTiVvY24Cjgy0n+EfgpsF/b9g1gb7o5wb8DDlqBY0uSJEmSVhOTJrpV9UCSo4H/XJEDVdX36D/vFuDZfeoXcOiKHFOSJEmStPoZdujyecC2MxmIJEmSJEmjMOzXC30S+FCSJwMXAnf3bqyqi0YdmCRJkiRJ0zFsoru4/T6mz7YCFowmHEmSJEmSVsywie5mMxqFJEmSJEkjMlSiW1U/melAJEmSJEkahaG/RzfJXkm+nuSKJBu3slcmWW7FZEmSJEmSZstQiW6SlwBfBq6hG8b88LZpAfCWmQlNkiRJkqSpG7ZH9y3AP1XVG4AHesrPA7YZeVSSJEmSJE3TsInu5sC5fcrvAv54dOFIkiRJkrRihk10bwKe2qd8N+C60YUjSZIkSdKKGTbRXQQcl2Tn9nzjJAcCHwCOn5HIJEmSJEmahmG/XugDSdYCTgceCZwJ/B74YFV9bAbjkyRJkiRpSoZKdAGq6u1J3gNsRdcTfEVV3TVjkUmSJEmSNA1DJ7pNAfe2x8tGHIskSZIkSSts2O/RfUSSjwC3A5cAlwK3Jzk2ySNnMkBJkiRJkqZi2B7d44E9gVfy0NcM7QS8D3gs8IrRhyZJk7vqrKtmOwRpKFvsvsVshyBJ0mpj2ER3P+Bvq+r0nrLrk9wKnIiJriRJkiRpjhj264XuBn7ep/znwD2jC0eSJEmSpBUzbKL7UeCdSdYcK2iP/6VtkyRJkiRpThg4dDnJKeOKdgd+nuTS9vzP2+sfPTOhSZIkSZI0dRPN0f3VuOcnjnv+4xHHIkmSJEnSChuY6FbVQSszEEmSJEmSRmHYObqSJEmSJK0Shvp6oSSPB44E9gDWY1yCXFXrjTwySZIkSZKmYdjv0T0B2Br4LHALUDMWkSRJkjSPXP2V2Y5AGs5zZzuAERo20d0d+MuqumgGY5GkKfvpx++f7RCkoWyx+2xHIEnS6mPYObrXTaGuJEmSJEmzZtge3cOB9yX5n8BlVbVsBmOa1xy6olXFfBq6IkmSpNXLsInutcCawEUASf7bxqpaMNqwJEmSJEmanmET3S8AawGH4WJUkiRJkqQ5bNhEdyGwfVVdNpPBSJIkSZK0ooZdYOoK4I9nMhBJkiRJkkZh2ET3HcAxSZ6TZP0ka/f+DLODJJ9OcmuSy3rK1k5yepJr2u/Ht/IkOS7JtUkuTbLt1N+aJEmSJGl1NGyi+w1ge+A04Cbgtvbzy/Z7GJ8Bnjeu7AjgjKraHDijPQfYC9i8/RwMHD/kMSRJkiRJq7lh5+jusaIHqqolSTYdV7wPsHt7/FngLOCtrfyEqirgvCSPS7JBVd28onFIkiRJkua3oRLdqjp7ho6//ljyWlU3J1mvlW8I/Kyn3o2tbLlEN8nBdL2+bLLJJjMUpiRJkiRpVTFUojvZHNmqumg04Tx0yH6HGXDsRcAigIULF/q1R5IkSZK0mht26PIFdIlmbwLam1QumObxbxkbkpxkA+DWVn4jsHFPvY3o5gZLkiRJkjShYRej2gx4Svu9GfBU4ABgKfD8FTj+KcCB7fGBwMk95S9rqy/vCNzp/FxJkiRJ0jCGnaP7kz7F1ya5E3gn8M3J9pHkC3QLT62T5Mb2uqOALyf5R+CnwH6t+jeAvYFrgd8BBw0TpyRJkiRJww5dHuTHwDbDVKyqFw/Y9Ow+dQs4dAXikiRJkiStpoZdjGrt8UXABsCRwFUjjkmSJEmSpGkbtkf3lyy/6nHovgJo/5FGJEmSJEnSChg20d1j3PMHgduAa6vqgdGGJEmSJEnS9A27GNXZMx2IJEmSJEmjMGGi22dubl9VdftowpGkqbn6K7MdgTSc5852AJIkrUYm69HtNzd3vBpiP5IkSZIkrRSTJajj5+b2eh5wOOAcXUmSJEnSnDFhottvbm6SbYH3A7sBnwDeNTOhSZIkSZI0dQ8btmKSzZIsBr4P3A5sVVWHVdVtMxadJEmSJElTNGmim+QJSY4FfgQ8EdipqvavqutmPDpJkiRJkqZowkQ3yduA64C/BPapqr+qqgtWSmSSJEmSJE3DZItRvRu4B7gROCTJIf0qVdULRh2YJEmSJEnTMVmiewKTf72QJEmSJElzxmSrLr98JcUhSZIkSdJIDL3qsiRJkiRJqwITXUmSJEnSvGKiK0mSJEmaV0x0JUmSJEnziomuJEmSJGleMdGVJEmSJM0rJrqSJEmSpHnFRFeSJEmSNK+Y6EqSJEmS5hUTXUmSJEnSvGKiK0mSJEmaV0x0JUmSJEnziomuJEmSJGleMdGVJEmSJM0rJrqSJEmSpHnFRFeSJEmSNK+Y6EqSJEmS5hUTXUmSJEnSvDKnE90kz0tyVZJrkxwx2/FIkiRJkua+OZvoJlkAfAzYC9gKeHGSrWY3KkmSJEnSXDdnE11ge+Daqrq+qu4DvgjsM8sxSZIkSZLmuFTVbMfQV5IXAc+rqle25/8A7FBVrx1X72Dg4PZ0C+CqlRqo5oJ1gF/OdhDSPGO7kkbLNiWNnu1q9fTkqlp3skprrIxIpil9ypbLyqtqEbBo5sPRXJXkgqpaONtxSPOJ7UoaLduUNHq2K01kLg9dvhHYuOf5RsBNsxSLJEmSJGkVMZcT3R8AmyfZLMkfAQcAp8xyTJIkSZKkOW7ODl2uqgeSvBb4NrAA+HRVXT7LYWlucui6NHq2K2m0bFPS6NmuNNCcXYxKkiRJkqTpmMtDlyVJkiRJmjITXUmSJEnSvGKiq5UqybIkFye5JMlFSZ61Eo/98iQPJnl6T9llSTZtj29IsrTFdlqSJ66s2LRqSbJ+ksVJrk9yYZJzk7xwhPt/2wTbXtE+p5e2z+8+IzjepkkuW9H99NlnJXlXT9k6Se5P8n/a832TbDWi492Q5MSe5y9K8pn2+OVJbmv/e65I8k+jOKbmpnS+l2SvnrK/T/KtCV5zY5LHJVkjyR0zFNcbkzxyJvbdc4zntHbX+96/lWSX9vh7Sa5q57nvJdl8JuPR6mE6bW4GYliQ5Jz2+ClJDpji69dobef9PWVHJHlHe/zuJD9v55GlSf56tO9AM8FEVyvbPVW1TVU9A/hn4H3jKyRZMIPHvxF4+wTb92ixXQAMTDa0+koS4GvAkqp6SlU9k25V+I361J3ugn99P3tJNqL7/O5SVU8HdgQuneYxVobrgef3PN8P6F1UcF9gJIluszDJ1gO2famqtgF2B96bZP0RHldzSHWLj7waOCbJI5M8GngPcOjsRsYbgRlNdJufAe+YYPv+7Ty3GHj/BPWkocyFNldVy6pq1/b0KXTn5am6B/j7JGsP2H50O4+8GPhMux7QHGaiq9n0x8CvAZLsnuTMJIuBpUneleTwsYpJ3pPksPb4LT09r0e1sj9pd60vTHJOkj8bcMyvA1sn2WKS2JYAf7qib1Dz0l8B91XV/x0rqKqfVNVH4Q+9h19JcipwWit7c5IftF7Yfx17XZKvtc/s5UkObmVHAWu2u8afH3fs9YDfAne1495VVT9urzsryYeTLElyZZLtkpyU5Jok7+455htbT/BlSV4//s21O+E/bK9fkOTonthf1ep8Lj09yUk+n+QFff5W9wBXJlnYnu8PfLm95lnAC4Cj23v9k/Ye3p/k/CRXJ9m11d26lV3c4hjUC/VBJrlBVVW3AtcBT56onlZtVXUZcCrwVuCdwAlVdV2SA3s+Sx9PMvA6KMnDkhzT2srSJC9q5YuS7N0en5pkUXv8qiRHJnlskm+2c9Rl6UYXvIGu/Z6T5Dut/kvbfi9L8t5WtkaSO5Ic1V5/bpL12rb1W5u+oL2HHQeEfhFwb5I9JvkzeZ7TyEzQ5t7Sc855HUC/NtLKt0tydjsvfjPthmS63uJj2vXdFUkWJvlqO78d2er0jsY4CtijtfPD2rZjWru5NMkrB7yN+4BPA4cP2N77XgM8fkX+Zpp5c/brhTRvrZnkYrq72hvQJQ1jtgeeVlU/Tjec+CTg2HYhcgCwfbphMfsCO1TV7/LQXbdFwKur6pokOwAfH7fvMQ8CH6C7GD5wgjifDyyd5nvU/LY13YXkRHYCnl5VtyfZE9ic7vMd4JQku1XVEuAVrc6awA+SnFhVRyR5bbtrPN4lwC3Aj5OcAZxUVaf2bL+vqnZLd5PoZOCZwO3AdUk+DGwKHATs0GL5fpKzeeiG0xbAF4GDquridMn3nVW1XZJHAP+V5DTgU8AbgJOTrAU8i8Ht6YvAAUl+ASwDbgKeVFX/L8kpwNer6j/a8QHWqKrtWyLxTuA5dD0Fx1bV59N9r/qgUR9fBg5JMvDiPclT6O72XzuojuaNf6Vrq/fR9fY/DXgh8Kz2FYaL6M4tiwe8fj+6EQfPANala6NL6BLEXZN8E1gfWKfV3wX4DLA3cENV7QWQZK2qujPJm4Bdq+qOdKMz3g0sBO4EvpPk+cC3gLWAs9v/gmOAV9BduB8HfKCqzmvnyK8DTxsQ+3voenXPnODv8zd4ntNojW9z2wMvoTv/LQDOb+ecLRnXRto55ljgBVX1yyQvAd4FHNz2fU9V7dra0dfozm93Atcn+QjtBnBzBPDaqtq37f8Q4NZ2bnkEcF6S06rqp33ew0eBi5N8aNCbTHej9t6qun3qfyKtTCa6WtnuGbuAT7ITcEK7+AA4f6x3qqpuSPKrJH9BdyHxw6r6VZLnAP9eVb9r9W5P8hi6C+2v5KFRJI+YIIbFwNuTbNZn25lJltENB51o6JcEQJKP0V3g3ldV27Xi03tOgHu2nx+254+hS3yXAIflobm9G7fyXw06VlUtS/I8YDvg2cCHkzyzqo5sVU5pv5cCl1fVzS3G69v+dwG+WlV3t/KTgF3b69alS47/ruc7y/cEnj52t53uAnzzqjotycdaT9PfAidW1QMDwv4W3cXKLcCXBr23Hie13xfSJeYA59K12Y3okvtrBrx2GXA03bSIb47btn+6eYq/B17lBcr8V1V3J/kScFdV/b6dP7YDLmjnijXphvkOsguwuKqWAb9I8j26xPQc4DXAn9OdK57Y2sKOdDdlNgGOSjc649Sq+q8++94B+G5V/RIg3Wim3ejayz1VNfb5vZCujUJ302eLnvPc45OsWVX39Hnv3003MmqnPsf+UpJ76KYWvG6C9y9NSZ82tyvd+eF30I1iomtXZzKujSTZhu5G8nfaZ3wB3XSzMb3nt6VVdUvb5w10U4d+NEFoewJb5qF5u2vRnW+XS3TbjajFdMOux38H65uTvJxuZNX+k/09NPtMdDVrqurcJOvQXWAD3D2uyqeAlwNPpBtKAl0v1Ph/PA8D7hjQA9bvuA+0O3Vv7bN5j7ELD2mAy4G/G3tSVYe2z/EFPXV6P8sB3ldVn+jdSZLd6S5cd2qjE85iiPl7bS7U+XR3xk8H/h04sm3+ffv9YM/jsedrtFgGuZPuon9nHppHG+B1VfXtPvU/R3en/gC6HqdB8d6X5ELgTXQXMX8zQQy972FZi5mqWpzk+8BfA99O8sqq+u6A13+OLtG9fFz5l6rqtZMcW/PPg+0Hus/zp6vqX4Z8bd/2UlU/aYntnnQ3rJ5E1w5+1W4ijQ3X35tuaP7Xq+q9w+y7ua/n8R/aQXvN9lV13/Iv6es99F+TYv+qunjIfUhTNb7NLaeqlmsjdDcnL+2ZZzveZOe3iQQ4pKrOGCJ+gGOAH9CdT3rb29FV9ZEh96E5wDm6mjXp5tEuYHAP1leBsd6rsQvt04BXJHlU28faVfUbuqGc+7WyJHnGJIf/DF2Sse4k9aTxvgs8MslresoeNUH9b9N9Zh8DkGTDdpG8FvDrluT+GV1v0Jj7kzx8/I6SPCnJtj1F2wA/mULsS4B9kzwq3WIhL6TrnYLuZL4v8LIk/6Mn9teMxZLkqe110LWh1wP09AAP8iHgrVU1vq3/FnjsZEG34cbXV9VxdHf1nz6oblXdD3x4LDapx3foFppZByDJE5JsMkH9JXTD7hekmyu4Mw/d0Po+cFircw7w5vabJBvS9Wh9ju6CeazN9n7ez6ObQ/iEdIvWHQCcPUT8f1jcp/WADVRV36C7UTxogTZppi0BXphkzXYO3Idunnq/NnIFsGEb7kySP8rgxQUnM/7c8m26aS1rtH1vkW7KUF+tw+OrdJ0tWoXZo6uVbWyOLnR32A5swzGXq9h6gs6k661d1sq+1U7uFyS5D/gG3XzblwDHp1sG/uF08wIvGRRE2/dxdPNBpKFVVSXZl27Y8FuA2+h6cPuNEKAN890SOLd9zu8CXko3RPHVSS4FrqK78B2zCLg0yUVV9ZKe8ocDH0zyJODeduxXTyH2i9J95c75rehTVfXDNt9vbNjZ84HTk9xNN6piU+CidMHfRpcMU1W3JLmSbq7UZMe9nOV7WKFrp59Mt9Dci/psH7M/8NIk9wO/AP73JIf8N5x6oHGqamm6xeC+k27th/vp2k+/eXoA/0F3A+oSupFEb2yLmUGX1O7WptncRDdPd+ym0TPohmU+SHcDaayNLmrH/llVPSfJ/wLOojsXnlpV/5mJV2o/lO48dxDd9duZTL6q7XuBEyepI82Iqjo/yRfoekcBjm/tcG/GtZE21PlFwHFJHkv3Gf8Q/c8dk/khsCDJJXTng4/RTSm4uJ2Hb6VLuidyNHDINI6tOSTdKDhp7mkXIhcB+00wJ0/SLGijKpYC21bVnbMdjyRJUi+HLmtOSrIV3aqoZ5jkSnNLW9TnR8BHTXIlSdJcZI+uJEmSJGlesUdXkiRJkjSvmOhKkiRJkuYVE11JkiRJ0rxioitJkiRJmldMdCVJkiRJ88r/B96VgIhX4W1TAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 1152x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sheep_kind_observed = sheep_observations.pivot(columns='common_names', index='park_name', values = 'observations').reset_index()\n",
    "\n",
    "varBSBS = sheep_kind_observed['Bighorn Sheep, Bighorn Sheep']\n",
    "varDS = sheep_kind_observed['Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)']\n",
    "varSNBS = sheep_kind_observed['Sierra Nevada Bighorn Sheep']\n",
    "\n",
    "xval = range(len(sheep_kind_observed))\n",
    "plt.figure(figsize=(16,4))\n",
    "ax=plt.subplot()\n",
    "p1=plt.bar(xval, varDS, color='darkviolet')\n",
    "p2=plt.bar(xval, varBSBS, bottom = varDS, color = 'mediumorchid')\n",
    "p3=plt.bar(xval, varSNBS, bottom = (varDS+varBSBS), color= 'thistle')\n",
    "ax.set_xticks (xval)\n",
    "parks = ['Bryce NP', 'Great Smokey Mtns NP', 'Yellowstone NP', 'Yosemite NP']\n",
    "ax.set_xticklabels (parks)\n",
    "plt.legend((p1[0], p2[0], p3[0]), ('Domestic Sheep - No Protection', 'Bighorn Sheep - Protection Concerns', 'Sierra Nevada Bighorn Sheep - Endangered'))\n",
    "\n",
    "ax.set_ylabel('Number of Observations', size='14')\n",
    "ax.set_title ('Observations of Sheep per Week', size='20')\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Our scientists know that 15% of sheep at Bryce National Park have foot and mouth disease.  Park rangers at Yellowstone National Park have been running a program to reduce the rate of foot and mouth disease at that park.  The scientists want to test whether or not this program is working.  They want to be able to detect reductions of at least 5 percentage point.  For instance, if 10% of sheep in Yellowstone have foot and mouth disease, they'd like to be able to know this, with confidence.\n",
    "\n",
    "Use the sample size calculator at <a href=\"https://www.optimizely.com/sample-size-calculator/\">Optimizely</a> to calculate the number of sheep that they would need to observe from each park.  Use the default level of significance (90%).\n",
    "\n",
    "Remember that \"Minimum Detectable Effect\" is a percent of the baseline."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 608,
   "metadata": {},
   "outputs": [],
   "source": [
    "numSheep = 35000"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "How many weeks would you need to observe sheep at Bryce National Park in order to observe enough sheep?  How many weeks would you need to observe at Yellowstone National Park to observe enough sheep?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "bryce_count = numSheep/(obs_by_park.observations[0])\n",
    "print bryce_count\n",
    "\n",
    "ynp_count = numSheep/(obs_by_park.observations[2])\n",
    "print pynp_count"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 609,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "140\n",
      "69\n"
     ]
    }
   ],
   "source": [
    "bryce_count = numSheep/(obs_by_park.observations[0])\n",
    "yellow_count = numSheep/(obs_by_park.observations[2])\n",
    "print bryce_count\n",
    "print yellow_count"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.14"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
