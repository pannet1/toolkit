# contributing

To create a new feature branch on Git and commit changes, you can follow these steps:

1. **Ensure you're on the main branch**: Before creating a new feature branch, it's good practice to ensure you're working on the latest version of the main branch. You can do this by running:
   ```bash
   git checkout main
   git pull origin main
   ```

2. **Create a new branch**: Now, create a new branch for your feature. Replace `feature-branch-name` with an appropriate name for your feature:
   ```bash
   git checkout -b feature-branch-name
   ```

3. **Make changes**: Make your desired changes to the code, whether it's adding new features, fixing bugs, or making improvements.

4. **Stage the changes**: Stage the changes you want to commit. You can do this for individual files or all files using:
   ```bash
   git add <file1> <file2> ...
   ```
   Or to add all changes:
   ```bash
   git add .
   ```

5. **Commit the changes**: Commit your changes to the feature branch:
   ```bash
   git commit -m "Your commit message here"
   ```

6. **Push the branch**: Push the feature branch to the remote repository:
   ```bash
   git push origin feature-branch-name
   ```

Now, your changes are committed to the new feature branch in the remote repository. You can continue working on this branch, and when you're ready, you can merge it back into the main branch via a pull request.
