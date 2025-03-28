# GitHub Pages Deployment Instructions

This document provides step-by-step instructions for deploying your AI Evangelist website to GitHub Pages.

## Prerequisites

1. A GitHub account (create one at [github.com](https://github.com) if you don't have one)
2. Git installed on your computer (download from [git-scm.com](https://git-scm.com/downloads))

## Deployment Steps

### 1. Create a New GitHub Repository

1. Log in to your GitHub account
2. Click the "+" icon in the top-right corner and select "New repository"
3. Name your repository (e.g., "ai-evangelist-website")
4. Make the repository public
5. Do not initialize with a README, .gitignore, or license
6. Click "Create repository"

### 2. Upload Your Website Files

#### Option 1: Using GitHub Web Interface

1. In your new repository, click "uploading an existing file" link
2. Drag and drop all the files and folders from the extracted zip file
3. Commit the changes with a message like "Initial website upload"

#### Option 2: Using Git Command Line (Recommended)

1. Extract the `github_pages_deployment.zip` file to a folder on your computer
2. Open a terminal or command prompt
3. Navigate to the extracted folder:
   ```
   cd path/to/extracted/folder
   ```
4. Initialize a Git repository:
   ```
   git init
   ```
5. Add all files to the repository:
   ```
   git add .
   ```
6. Commit the files:
   ```
   git commit -m "Initial website upload"
   ```
7. Link to your GitHub repository:
   ```
   git remote add origin https://github.com/YOUR-USERNAME/ai-evangelist-website.git
   ```
   (Replace YOUR-USERNAME with your GitHub username and ai-evangelist-website with your repository name)
8. Push the files to GitHub:
   ```
   git push -u origin master
   ```
   or if you're using the main branch:
   ```
   git push -u origin main
   ```

### 3. Enable GitHub Pages

1. Go to your repository on GitHub
2. Click "Settings" tab
3. Scroll down to the "GitHub Pages" section
4. Under "Source", select "main" or "master" branch
5. Click "Save"
6. Wait a few minutes for GitHub to build and deploy your site
7. Your website will be available at: `https://YOUR-USERNAME.github.io/ai-evangelist-website/`

## Custom Domain (Optional)

If you want to use a custom domain:

1. In the GitHub Pages section of your repository settings
2. Enter your domain in the "Custom domain" field
3. Click "Save"
4. Configure your domain's DNS settings to point to GitHub Pages:
   - Type: A Record
   - Name: @ or subdomain
   - Value: GitHub Pages IP addresses (provided in GitHub documentation)

## Updating Your Website

To update your website in the future:

1. Make changes to your local files
2. Commit the changes:
   ```
   git add .
   git commit -m "Description of changes"
   git push
   ```
3. GitHub will automatically rebuild and deploy your site

## Troubleshooting

- If your site doesn't appear, check the GitHub Pages section in repository settings for any error messages
- Ensure all file paths in your HTML are relative, not absolute
- Check that all required files are included in the repository
- Verify that GitHub Pages is enabled for the correct branch

## Additional Resources

- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Custom Domain Setup Guide](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)
