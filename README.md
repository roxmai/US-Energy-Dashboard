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