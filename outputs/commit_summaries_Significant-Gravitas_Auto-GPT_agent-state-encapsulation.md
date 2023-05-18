On 2023-05-16, amokduke made a commit titled "Adds check for Python 3.10 and print error message if required version not detected" (#3598). The commit includes the following changes:

- Updated the `run.sh` script to check for Python 3.10 and above.
- Provided informative error messages for unsupported Python versions.
- The changes consist of 12 additions and 8 deletions in the `run.sh` file.

This commit ensures that Auto GPT only runs on systems with Python 3.10 or higher and prompts users to install the required version if not detected. The commit is co-authored by merwanehamadi.
---
Commit Message: Huggingface retry generate_image with delay (#2745)

In this commit, the generate_image_with_hf function in `autogpt/commands/image_gen.py` has been updated to handle retries when there's an error in the API response. There's now a retry loop with a maximum of 10 attempts, and it will wait for a specified delay before retrying when the returned error contains an estimated time. Additional test cases have also been added to `tests/test_image_gen.py` to test these new failure scenarios in the huggingface image generation process.
---
2023-05-16T14:10:33Z: Stefan Ayala made a commit, titled 'Allow absolute paths if contained in workspace (#3932)', in which he suggests allowing access to absolute paths if they are within the workspace. Co-authored by k-boikov, the commit modifies the file 'autogpt/workspace/workspace.py' with 2 additions and 1 deletion. The main change involves adding a condition to check if the absolute path is contained within the workspace directory before raising a ValueError.
---
Date: 2023-05-16

Commit Message: Clarify .env.template image-provider options (#3720)

Summary:
Cenny made a commit to improve and clarify the image-provider options in the .env.template file. The changes include consolidating duplicate options, simplifying the instructions, and providing clearer guidance for the user. The image-provider options mentioned are 'dalle', 'huggingface', and 'sdwebui', and image sizes for 'dalle' include 256, 512, and 1024. The commit includes some co-authors as well.
---
In this commit, a legal warning was added for the continuous mode of the AutoGPT system. This warning appears as a disclaimer and indemnification agreement that users must read carefully before using the continuous mode. The warning covers details such as an introduction to the system, no liability for actions of the system, user responsibility, and indemnification. This commit modifies two files: `autogpt/main.py` and `autogpt/utils.py`. In `autogpt/main.py`, the code was added to display the legal warning if continuous mode is enabled. In `autogpt/utils.py`, the `get_legal_warning()` function was added containing the legal text.
---
Date: 2023-05-16T15:14:24Z
Author: amokduke
Co-Author: merwanehamadi
PR: #3598
Commit Message: Adds check for Python 3.10 and print error message if required version not detected.

Summary:
- The `run.sh` script was updated to check for Python version 3.10 and above.
- An informative error message is printed if an unsupported Python version is detected.
- The script continues to check for missing packages and installs them if required, when the Python version is 3.10 or higher.

Details:
- 1 file changed: `run.sh`
- 12 additions and 8 deletions
- 20 total changes
---
Commit Summary:
- Date: 2023-05-16T15:02:55Z
- Author: Kory Becker
- PR Title: Huggingface retry generate_image with delay (#2745)

This commit adds retry functionality with delay for generating images using Huggingface API. In `autogpt/commands/image_gen.py`, the `generate_image_with_hf` function has been modified to retry with a delay if the API response is not ok. The delay is determined based on the `estimated_time` received in the API error response. The retry will be attempted up to 10 times before considering it a failed attempt.

Additionally, various test cases have been added in `tests/test_image_gen.py` to cover different scenarios such as successful image generation, failing requests with and without delay, invalid JSON response, and missing API token. Some tests have been marked as XFAIL due to external dependencies or issues with the API call.

The commit includes contributions from multiple authors.
---
On 2023-05-16, Stefan Ayala made a commit titled "Allow absolute paths if contained in workspace (#3932)", with a co-author named k-boikov. The commit modifies the 'autogpt/workspace/workspace.py' file, making a change to the conditional check for absolute paths. The previous implementation disallowed absolute paths, whereas now absolute paths are allowed if they are contained in the workspace directory. The total changes include two additions and one deletion.
---
Title: Clarify .env.template image-provider options (#3720)

Summary:
This commit clarifies the image-provider options in the .env.template file for configuration settings. It consolidates duplicate options and provides guidance on the available image providers (dalle, huggingface, or sdwebui) and the corresponding image sizes for the dalle provider (256, 512, 1024).
---
### Commit Summary - Legal warning on continuous run (#4239)
---

**Author:** Nicholas Tindle

**Date:** 2023-05-16

**Changes:**

- Added a legal warning to be displayed when the AutoGPT system is run in continuous mode.
- The legal warning contains a disclaimer, indemnification agreement, and outlines user responsibility and liability.
- The legal warning text is defined in the `get_legal_warning()` function in `autogpt/utils.py`.

**Files modified:**
1. `autogpt/main.py` - Added a call to display the legal warning in continuous mode.
2. `autogpt/utils.py` - Added `get_legal_warning()` function, which returns the legal warning text.
---
### Commit Summary:

**Author:** Malahieude Timothé

**Co-authored-by:** Nicholas Tindle

**Commit Date:** 2023-05-16T04:20:14Z

**Commit Message:** Fix ai_name not passed to Agent (#3948)

**Changes:**
- A diff was made in `autogpt/main.py`.
- Two lines of code were added and no lines were deleted.
- The added code checks if `ai_config.ai_name` exists, and if it does, assigns its value to `ai_name`.

This commit fixes the issue where `ai_name` was not being passed to the Agent properly.
---
On May 16, 2023, a commit titled "fix ci cassettes (#4234)" was made by merwanehamadi, co-authored by Nicholas Tindle. This commit modifies two files: `.github/workflows/add-cassettes.yml` and `.github/workflows/ci.yml`.

In the `add-cassettes.yml` file, the changes involve updating the `git reset` and `branch` commands to use the sha of the pull request's head commit instead of the pull request number.

In the `ci.yml` file, the changes include storing the current commit sha in the `COMMIT_SHA` variable before committing the cassettes. Additionally, the `git checkout` and `git push` commands are modified to use the `COMMIT_SHA` variable, replacing the pull request number previously used.

These changes help ensure a more reliable relationship between the pull requests and their respective cassette updates.
---
#### Commit Summary

On 2023-05-16, gravelBridge committed the changes with the message "Added feature to interrupt y -N continuous commands (#4230)".

This commit adds a feature that allows users to interrupt the continuous execution of y -N commands. A signal handler was introduced to listen for interrupt signals (SIGINT). If the signal is received and there is an ongoing continuous operation, it stops the continuous command execution. The additions include 16 lines of code and were made in the 'autogpt/agent/agent.py' file.
---
