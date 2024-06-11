[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/A55IPDGc)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=15225700&assignment_repo_type=AssignmentRepo)

# README

### Project Information

**Description**
This tool's intended use is to summarize statistics for Continental US Natural Gas and Electrical Power consumption. Data is organized in a monthly time series and can be summarized by state or region.

**How to use:**
Insert description on how to use tool later

**Data sources:**

Electricity consumption by state, sector: "https://www.eia.gov/electricity/data/browser/#/topic/5?agg=0,1&geo=vvvvvvvvvvvvo&linechart=ELEC.SALES.TX-ALL.M~ELEC.SALES.TX-RES.M~ELEC.SALES.TX-COM.M~ELEC.SALES.TX-IND.M&columnchart=ELEC.SALES.TX-ALL.M~ELEC.SALES.TX-RES.M~ELEC.SALES.TX-COM.M~ELEC.SALES.TX-IND.M&map=ELEC.SALES.US-ALL.M&freq=M&start=200101&end=202403&ctype=linechart&ltype=pin&rtype=s&maptype=0&rse=0&pin=&endsec=vg"

Natural gas consumption: "https://www.eia.gov/dnav/ng/ng_cons_sum_a_EPG0_vgt_mmcf_m.htm"

Degree Day information and why it is used: "https://www.eia.gov/energyexplained/units-and-calculators/degree-days.php"
HDD: "https://www.eia.gov/totalenergy/data/browser/index.php?tbl=T01.10#/?f=M&start=197301&end=202402&charted=32-10"
CDD: "https://www.eia.gov/totalenergy/data/browser/index.php?tbl=T01.11#/?f=M&start=197301&end=202402&charted=32-10"



### Roadmap

please check `docs\Rox's_EDA.ipynb`

## Next Steps

### What We Need from the User:

1. **Location**: Region; The user will specify the location they’re interested in (e.g., ‘California’).
2. **Date Range**: ask for specific year OR month: ask for specific data to filter the data. 
 

### Steps:
1. **Ask for Inputs**: We'll prompt the user to enter the region and date range. If they input incorrectly, we’ll give them a friendly message to try again.
2. **Filter the Data**: Use the inputs to get the relevant slice of our dataset.
3. **Plot the Data**: create a plot using Matplotlib and save it as a PNG file.

### How It Works:
- **Input Prompts**: Clear and simple instructions for the user to follow:
    - State/Region name (e.g., 'California')
    - Date Seletion (YYYY OR MM)


- **Output**: Summary of all data
    - Electrical consumption (highest, lowest, average)
    - Natural gas consumption (highest, lowest, average)
    - Total energy consumption (highest, lowest, average)
    - Weather (highest, lowest, average)
    - plots showing the energy consumption and weather based on inputs.



### Branching Strategy for Python Group Project 

  

**Branch Naming Convention:** 

  

- **Feature Branches:** Use the format `issueNumber-description` 

  - Example: `01-add-readme`, `02-create-login` 

  

--- 

  

#### Steps and Git Commands 

  

1. **Sync with Main Branch**: 

    - Fetch and pull the latest code from the `main` branch: 

    ```bash 

    git fetch origin 

    git pull origin main 

    ``` 

  

2. **Create a Feature Branch**: 

    - Based on the issue you are working on, create a new branch from `main`: 

    ```bash 

    git checkout -b issueNumber-description main 

    ``` 

    - Example:  

    ```bash 

    git checkout -b 01-add-readme main 

    ``` 

  

3. **Local Development**: 

    - Develop your feature in the new branch. Regularly commit changes: 

    ```bash 

    git add . 

    git commit -m "Add detailed commit message here" 

    ``` 

  

4. **Local Testing**: 

    - Ensure your changes are thoroughly tested locally before pushing to GitHub. 

  

5. **Push to Remote**: 

    - Push your feature branch to the origin: 

    ```bash 

    git push origin issueNumber-description 

    ``` 

  

6. **Create a Pull Request (PR)**: 

    - Navigate to GitHub and create a Pull Request from your feature branch to the `main` branch. 

  

7. **Request Review**: 

    - Assign the PR to a team member for review. Ensure review and feedback are addressed. 

  

8. **Merge PR**: 

    - Once approved, **do not merge directly to `main`**. Use GitHub's merge functionality to complete the PR: 

    - The reviewer or the person responsible for maintaining the repository should merge the PR using GitHub's interface. 


### Creating Your Virtual Environment

Create a virtual environment in your workspace. In your virtual environment, you will have greater visibility of installed modules and their versions. This allows you to have better control the module versions, protecting your project from version inconsistencies.

#### Steps to create your virtual enviroment:

Please review [Official Documentation for venv - virtual environments](https://docs.python.org/3/library/venv.html). Our project will make use of venv.

1. **Confirm your working directory**:

    - To confirm working directory, typing "cd" into your terminal will navigate you to your current working directory

2. **Initialize your .venv virtual environment**

    - Create your .venv Virtual Environment by entering the command "python -m venv .venv" into your terminal
    - This command creates a new folder named '.venv' in your local workspace
    - If you expand the folder to inspect its contents, you will find installed modules inside the \Lib\ folder
    - Notice that .venv is included in the .gitignore. This means that is important that your virtual environment has the same name, or if it doesn't, you should add the name of your virtual environment to the .gitignore as a new line

    ```terminal
    
    Windows: python -m venv .venv
    Unix: python3 -m venv .venv

    ```

3. **Install required modules located in requirements.txt**

    - Enter command "pip install -r requirements.txt" into your local terminal
    - This command will update your .venv Virtual Environment to contain the requirements listed in the requirements.txt file
    - You should do this everytime you make a new branch to update your .venv Virtual Environment to the latest version of requirements.txt
    
    ```terminal
    
    Windows: python -m venv .venv
    Unix: python3 -m venv .venv

    ```

4. **Activate your .venv**

    - Enter command ".venv/Scripts/activate" into your local terminal
    - This command will activate your Virtual Environment - you should see it activated in your terminal. If you do not see your '(.venv)' as active in your terminal, you may have to try again
    - You should do this everytime you make a new branch to update your .venv Virtual Environment to the latest version of requirements.txt

    ![screenshot1](https://github.com/ENSF-692-Spring-2024/ensf-692-project-the-cool-company/blob/main/screenshot_1_venv.png "Activate .venv")
    
    ```terminal
    
    .venv/Scripts/activate

    ```

5. **Update requirements.txt**

    - Enter the command "pip freeze > requirements.txt" into your local terminal
    - You will want to do this everytime you install new modules via pip install to ensure all users have the most up to date environment


    ```terminal
    
    pip freeze > requirements.txt

    ```







