# Deploying Your AI Evangelist Website to Azure Static Web Apps

This comprehensive guide will walk you through deploying your AI Evangelist website to Microsoft Azure using Azure Static Web Apps. This service is designed specifically for static websites like yours and offers many benefits including global distribution, built-in security, and seamless integration with other Azure services.

## Prerequisites

1. **Microsoft Azure Account**: If you don't have one, you can create a free account at [azure.microsoft.com](https://azure.microsoft.com/en-us/free/)
2. **Your Website Files**: The files from the `github_pages_deployment.zip` package we prepared earlier
3. **GitHub Account**: For the easiest deployment method (optional, but recommended)

## Deployment Options

There are two main ways to deploy your website to Azure Static Web Apps:

1. **GitHub Integration** (Recommended): Connect your GitHub repository to Azure for automatic deployments
2. **Direct Upload**: Upload your website files directly through the Azure portal

This guide will cover both methods, starting with the recommended GitHub integration approach.

## Method 1: Deploying via GitHub Integration

### Step 1: Prepare Your GitHub Repository

If you haven't already created a GitHub repository with your website files:

1. Create a new GitHub repository (e.g., "ai-evangelist-website")
2. Upload all files from the `github_pages_deployment.zip` package to this repository
3. Make sure your main HTML file is named `index.html` and is in the root directory

### Step 2: Create an Azure Static Web App

1. Sign in to the [Azure Portal](https://portal.azure.com)
2. Click on "Create a resource" in the top-left corner
3. Search for "Static Web App" and select "Static Web App"
4. Click "Create"

### Step 3: Configure the Basic Settings

1. **Subscription**: Select your Azure subscription
2. **Resource Group**: Create a new one (e.g., "ai-evangelist-resources") or use an existing one
3. **Name**: Enter a name for your app (e.g., "ai-evangelist")
4. **Plan type**: Select "Free" for testing or "Standard" for production use
5. **Region**: Choose a region close to your target audience (e.g., "UK South" for UK-based visitors)
6. Click "Next: Deployment" to continue

### Step 4: Configure Deployment Settings

1. **Deployment source**: Select "GitHub"
2. Click "Sign in with GitHub" and authorize Azure to access your GitHub account
3. Select your:
   - **Organization**: Your GitHub username or organization
   - **Repository**: The repository containing your website (e.g., "ai-evangelist-website")
   - **Branch**: The branch to deploy (usually "main" or "master")
4. Under "Build Details":
   - **Build Preset**: Select "Custom"
   - **App location**: Enter "/" (the root of your repository)
   - **Api location**: Leave empty (as this is a static website without an API)
   - **Output location**: Leave empty (as your built files are already in the root)
5. Click "Review + create"

### Step 5: Review and Create

1. Review all your settings
2. Click "Create" to deploy your Static Web App

Azure will now create your Static Web App and set up a GitHub Action in your repository. This GitHub Action will automatically build and deploy your website whenever you push changes to your repository.

### Step 6: Access Your Website

1. Once deployment is complete, click "Go to resource"
2. On the overview page, you'll find the URL of your website (e.g., https://blue-field-0123456789abcdef.azurestaticapps.net)
3. Click on this URL to view your deployed website

## Method 2: Direct Upload via Azure Portal

If you prefer not to use GitHub, you can deploy directly through the Azure Portal:

### Step 1: Create an Azure Static Web App

1. Sign in to the [Azure Portal](https://portal.azure.com)
2. Click on "Create a resource" in the top-left corner
3. Search for "Static Web App" and select "Static Web App"
4. Click "Create"

### Step 2: Configure the Basic Settings

1. **Subscription**: Select your Azure subscription
2. **Resource Group**: Create a new one or use an existing one
3. **Name**: Enter a name for your app (e.g., "ai-evangelist")
4. **Plan type**: Select "Free" for testing or "Standard" for production use
5. **Region**: Choose a region close to your target audience
6. Under "Deployment details", select "Other" as the deployment source
7. Click "Review + create", then "Create"

### Step 3: Upload Your Website Files

1. Once the Static Web App is created, go to the resource
2. In the left menu, click on "Configuration"
3. Note the "API key" value - you'll need this for authentication
4. Open a command prompt or terminal on your computer
5. Navigate to the directory containing your extracted website files
6. Install the Azure Static Web Apps CLI:
   ```
   npm install -g @azure/static-web-apps-cli
   ```
7. Deploy your website:
   ```
   swa deploy ./path-to-your-website-files --api-key YOUR_API_KEY --env production
   ```
   (Replace YOUR_API_KEY with the API key from step 3)

## Setting Up a Custom Domain (Optional)

To use your own domain (e.g., aievangelist.london) instead of the default Azure domain:

1. Go to your Static Web App in the Azure Portal
2. In the left menu, click on "Custom domains"
3. Click "Add"
4. Enter your domain name (e.g., "www.aievangelist.london")
5. Follow the instructions to validate your domain ownership:
   - Add the provided TXT record to your domain's DNS settings
   - Once validated, add the CNAME record to point your domain to Azure

## Security Best Practices

Azure Static Web Apps include several security features:

1. **Free SSL/TLS certificates**: Your site is automatically secured with HTTPS
2. **Azure Active Directory integration**: For securing admin access to your Azure resources
3. **Role-based access control**: Define who can manage your Static Web App in Azure

Additional security recommendations:

1. **Enable Azure Multi-Factor Authentication** for your Azure account
2. **Regularly update** your website content and dependencies
3. **Review access permissions** in your Azure subscription regularly
4. **Enable Azure Security Center** for advanced security monitoring

## Updating Your Website

### If using GitHub integration:

1. Make changes to your files locally
2. Commit and push to your GitHub repository
3. Azure will automatically rebuild and deploy your site

### If using direct upload:

1. Make changes to your files locally
2. Use the SWA CLI to redeploy:
   ```
   swa deploy ./path-to-your-website-files --api-key YOUR_API_KEY --env production
   ```

## Monitoring and Analytics

1. In your Static Web App resource, go to "Monitoring" in the left menu
2. You can view basic metrics like requests and errors
3. For more detailed analytics, consider setting up:
   - **Azure Application Insights**: For detailed performance monitoring
   - **Azure Monitor**: For alerts and dashboards

## Troubleshooting Common Issues

1. **Website not updating after push**: Check the GitHub Actions tab in your repository to see if there are any build errors
2. **Custom domain not working**: Verify your DNS settings and check if the validation is complete
3. **Deployment failures**: Check the deployment logs in the Azure Portal under your Static Web App resource

## Cost Management

Azure Static Web Apps has a free tier that includes:
- 100GB bandwidth per month
- 2 custom domains
- 500MB storage

For most small business websites, this free tier is sufficient. If you need more resources, the Standard tier costs approximately £7-9 per month.

## Additional Resources

- [Azure Static Web Apps Documentation](https://docs.microsoft.com/en-us/azure/static-web-apps/)
- [Azure Static Web Apps CLI](https://github.com/Azure/static-web-apps-cli)
- [Custom Domain Configuration](https://docs.microsoft.com/en-us/azure/static-web-apps/custom-domain)
