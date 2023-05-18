The commit clarifies and consolidates the options for the .env.template image-provider, simplifying the code and making it more intuitive. Co-authored by three contributors, the changes involve modifying the IMAGE_PROVIDER and IMAGE_SIZE options for the OPEN AI and COMMON SETTINGS sections, specifically for the dalle image provider. There were 6 changes made involving 3 additions and 3 deletions to the .env.template file.
---
Nicholas Tindle made a commit on May 16, 2023, which adds a legal warning on continuous run in the Auto-GPT project. The commit includes changes in `main.py` and `utils.py` files. The legal warning includes a disclaimer and indemnification agreement for using the Auto-GPT system and the responsibility of the user while operating the system.
---
On 2023-05-16T04:20:14Z, Malahieude Timothé made a commit with the message "Fix ai_name not passed to Agent (#3948)", which was co-authored by Nicholas Tindle. The commit modified the `autogpt/main.py` file, adding 2 lines of code to ensure that the `ai_name` variable is properly passed to the Agent class if it is specified in the configuration.
---
On 2023-05-16T03:43:21Z, merwanehamadi and Nicholas Tindle made a commit to fix CI cassettes in the Auto-GPT repository. The commit modified the `.github/workflows/add-cassettes.yml` file to update the branch name with the pull request head's SHA and the `.github/workflows/ci.yml` file to take the SHA before committing the cassette.
---
The commit added a feature to interrupt continuous commands using the "y -N" format. It also includes a signal handler to stop the execution of consecutive commands when an interrupt signal is received. The commit was co-authored by Nicholas Tindle.
---
The commit made on 2023-05-15T23:34:48Z by Boostrix includes updates related to showing the workspace during startup and fixing issue #2793. The code changes were made in the `autogpt/prompts/prompt.py` file, where the main AI configuration is constructed. If the restrict_to_workspace flag is set to True, a message is displayed indicating that all files/directories created by the agent can be found inside its workspace.
---
The commit made by Boostrix on May 15th, 2023 at 23:26:13Z improves the error message for a restriction on running local shell commands in the execute_python_file() function in the execute_code.py file. The commit adds the name of the config file, .env, where the EXECUTE_LOCAL_COMMANDS variable must be set to 'True' to allow shell command execution and warns against attempting to bypass this restriction. The commit was co-authored by k-boikov.
---
On 2023-05-15T19:54:40Z, k-boikov fixed an error in the `safe_google_results` function and added tests for it in the `test_google_search.py` file. The changes ensure that the results obtained from a Google search are safe for encoding. The commit also includes modifications in the `google_search.py` file and corresponding additions in the `test_google_search.py` file to improve the overall functionality and test coverage of the `google_search` and `google_official_search` functions.
---
This commit fixes an issue where commands with the same name were overwriting each other. The developer added a check to see if a command with the same name already exists and logs a warning message if so. They also added a logger and some debugging messages.
---
This commit by Reinier van der Leer on 2023-05-15T12:35:35Z patched the CI proxy. Specifically, it modified the `.github/workflows/ci.yml` file by replacing `vars.PROXY` with `secrets.PROXY` in the `PROXY` environment variable. The diff shows that one line was added and one line was removed, resulting in a total of two changes.
---
Based on the commit message, Pi merged changes from the "stable" branch into the "master" branch after the release of version 0.3.1. The diff for this commit shows that there were no changes made to any of the files in the repository. Therefore, it was likely a merge commit that didn't introduce any new changes to the code.
---
Based on the commit message and the empty diff, it seems that Pi merged the changes made in the "master" branch into the "stable" branch. Without further information, it's not possible to provide more details about the specific changes that were merged.
---
The commit made by k-boikov on 2023-05-14T13:30:10Z reverts the changes made previously to 'ci.yml' file where Python version 3.11 was put back as a requirement. The changes made in the previous commit were undone and the file was updated to only require Python version 3.10.
---
This commit by merwanehamadi, made on 2023-05-14T13:20:14Z, adds back version 3.11 to the list of Python versions to be checked in the ".github/workflows/ci.yml" file. The changes can be seen in the diff which shows a modification of the "python-version" list from ["3.10"] to ["3.10", "3.11"].
---
On 2023-05-14T02:31:24Z, merwanehamadi made a commit to remove Python 3.11 temporarily due to a rate limiting issue. The commit modified the `.github/workflows/ci.yml` file to only include Python 3.10 in the matrix.
---
The commit made by merwanehamadi on 2023-05-14T01:18:31Z with the message "Test New CI Pipeline (#4170)" introduced some changes to the CI pipeline workflow, according to the modified `.github/workflows/ci.yml` file. Additionally, they made a minor change in the `autogpt/llm/llm_utils.py` file related to an API error handling. The commit also included some empty commits and commits for pushing to the origin repository and adding an 's' to a quote.
---
On 2023-05-13T23:40:31Z, merwanehamadi pushed changes to the CI pipeline configuration file by replacing a hardcoded repository value with a variable that uses information from the pull request head repository. The commit also removed some double quotes that were no longer needed.
---
On 2023-05-13T23:25:56Z, merwanehamadi made a commit with the message "test new CI (#4168)" which modified the `.github/workflows/ci.yml` file to include a new `repository` parameter for both `jobs` in the YAML configuration. The diff for this commit shows two additions of the `repository` parameter in lines 25 and 67 of the file.
---
This commit by k-boikov adds the option "--install-plugin-deps" to the Docker entrypoint for running the "autogpt" Python package. This change was made in the Dockerfile and co-authored with Nicholas Tindle.
---
Abdelkarim Habouch added support for Edge browser using EdgeChromiumDriverManager in this commit. The commit also includes co-authors Nicholas Tindle and k-boikov. The changes include modifying .env.template to add 'edge' in the 'USE_WEB_BROWSER' note, and modifying web_selenium.py to add options for Edge browser and to use EdgeChromiumDriverManager.
---
Cenny made a commit on May 13, 2023, which fixed tests related to SD web UI functionality. The commit message shows that the fixed tests were failing due to the unavailability of the SD web UI. An external SD web UI may not be available. The diff shows changes made to some lines of code in the `test_image_gen.py` file.
---
Media made a commit on 2023-05-13T19:21:21Z with the message "Challenge: Kubernetes and documentation (#4121)." This commit includes changes to multiple files, including adding instructions for creating challenges for AutoGPT, defining an agent fixture for the Kubernetes challenge, and creating a test file for the Kubernetes challenge. The commit also includes linting, testing, and revisions to the code.
---
This commit adds functionality to show the number of preauthorized commands left in the Autogpt agent. It also adds logging to print the authorized commands left value. Three co-authors contributed to the commit.
---
Robin Richtsfeld made a commit on May 13, 2023, to fix the mock `Config` in the `milvus_memory_test.py` file. The commit was co-authored by k-boikov and the diff includes modifications to the `mock_config()` function. The new `mock_config()` function now returns a `MockConfig` object that inherits from `Config` and specifies the required attributes. The changes to the `mock_config()` function should enable successful testing of the `MilvusMemory` class.
---
On 2023-05-13T01:00:08Z, andrey13771 fixed a typo in the `autogpt/agent/agent.py` file by modifying a log message. The commit was co-authored by merwanehamadi, Richard Beales and k-boikov. The commit message was "fix typo in autopgt/agent/agent.py (#3747)". The commit included only one change with 2 lines modified and no additions or deletions.
---
On 2023-05-12T23:23:54Z, k-boikov made a commit with the message "Parse package versions so upgrades can be forced (#4149)." This commit adds functionality to parse package versions so that upgrades can be forced. Specifically, it changes the `installed_packages` variable to be a dictionary with package names as keys and package versions as values, and updates the logic for checking whether required packages are installed by parsing the package requirements with `pkg_resources.Requirement.parse()` and checking if the installed version meets the requirement specification.
---
