# Visual Step-by-Step Azure Deployment Guide

This guide provides visual instructions for deploying your AI Evangelist website to Azure Static Web Apps.

## Method 1: GitHub Integration Deployment (Recommended)

### Step 1: Sign in to Azure Portal

1. Go to [portal.azure.com](https://portal.azure.com)
2. Sign in with your Microsoft account

![Azure Portal Sign In](images/azure_signin.png)

### Step 2: Create a Static Web App

1. Click "Create a resource" in the top-left corner
2. Search for "Static Web App" and select it

![Create Resource](images/create_resource.png)
![Search Static Web App](images/search_static_web_app.png)

3. Click "Create"

![Create Static Web App](images/create_static_web_app.png)

### Step 3: Configure Basic Settings

Fill in the following information:

1. **Subscription**: Select your Azure subscription
2. **Resource Group**: Create new or use existing
3. **Name**: Enter "ai-evangelist" (or your preferred name)
4. **Plan type**: Select "Free"
5. **Region**: Choose "UK South" (or closest to your users)
6. Click "Next: Deployment"

![Basic Settings](images/basic_settings.png)

### Step 4: Configure Deployment Settings

1. **Deployment source**: Select "GitHub"
2. Click "Sign in with GitHub" and authorize Azure
3. Select your:
   - **Organization**: Your GitHub username
   - **Repository**: Your website repository
   - **Branch**: main (or master)
4. Under "Build Details":
   - **Build Preset**: Select "Custom"
   - **App location**: Enter "/"
   - **Api location**: Leave empty
   - **Output location**: Leave empty
5. Click "Review + create"

![Deployment Settings](images/deployment_settings.png)
![GitHub Authorization](images/github_auth.png)
![Build Details](images/build_details.png)

### Step 5: Review and Create

1. Review all settings
2. Click "Create"

![Review and Create](images/review_create.png)

### Step 6: Wait for Deployment

1. Azure will deploy your Static Web App
2. This process takes 2-5 minutes

![Deployment in Progress](images/deployment_progress.png)

### Step 7: Access Your Website

1. Once deployment completes, click "Go to resource"
2. On the overview page, find your website URL
3. Click the URL to view your deployed website

![Deployment Complete](images/deployment_complete.png)
![Website URL](images/website_url.png)
![Deployed Website](images/deployed_website.png)

## Method 2: Direct Upload via Azure CLI

### Step 1: Create Static Web App in Azure Portal

Follow Steps 1-3 from Method 1, but:
- In Step 3, under "Deployment details", select "Other"
- Complete the creation process

![Select Other Deployment](images/other_deployment.png)

### Step 2: Get Your API Key

1. Go to your Static Web App resource
2. In the left menu, click "Configuration"
3. Note the "API key" value

![API Key](images/api_key.png)

### Step 3: Install Azure Static Web Apps CLI

Open a command prompt or terminal on your computer and run:

```
npm install -g @azure/static-web-apps-cli
```

![Install CLI](images/install_cli.png)

### Step 4: Deploy Your Website

Navigate to your website files directory and run:

```
swa deploy ./path-to-your-website-files --api-key YOUR_API_KEY --env production
```

Replace YOUR_API_KEY with the key from Step 2.

![Deploy Command](images/deploy_command.png)
![Deployment Success](images/deployment_success.png)

## Setting Up a Custom Domain

### Step 1: Access Custom Domains

1. Go to your Static Web App in Azure Portal
2. In the left menu, click "Custom domains"
3. Click "Add"

![Custom Domains](images/custom_domains.png)
![Add Domain](images/add_domain.png)

### Step 2: Enter Domain Information

1. Enter your domain name (e.g., "www.aievangelist.london")
2. Click "Next: Validate"

![Enter Domain](images/enter_domain.png)

### Step 3: Validate Domain Ownership

1. Add the TXT record to your domain's DNS settings
2. Click "Next: Add record"

![Validate Domain](images/validate_domain.png)
![DNS Settings](images/dns_settings.png)

### Step 4: Add CNAME Record

1. Add the CNAME record to your domain's DNS settings
2. Click "Add"

![Add CNAME](images/add_cname.png)
![CNAME Settings](images/cname_settings.png)

### Step 5: Wait for Propagation

1. DNS changes can take 24-48 hours to propagate
2. Once complete, your custom domain will be active

![Domain Active](images/domain_active.png)

## Troubleshooting Common Issues

### Issue: Deployment Failed

**Solution**: Check GitHub Actions logs for errors

![GitHub Actions](images/github_actions.png)
![Deployment Logs](images/deployment_logs.png)

### Issue: Custom Domain Not Working

**Solution**: Verify DNS settings and check validation status

![DNS Verification](images/dns_verification.png)

### Issue: Website Not Updating

**Solution**: Check if your latest commit triggered a new deployment

![Check Deployments](images/check_deployments.png)

## Monitoring Your Website

### Step 1: Access Monitoring

1. Go to your Static Web App
2. In the left menu, click "Monitoring"

![Monitoring Menu](images/monitoring_menu.png)

### Step 2: View Metrics

1. Review requests, errors, and performance metrics
2. Set up alerts for important thresholds

![Monitoring Dashboard](images/monitoring_dashboard.png)
![Set Alerts](images/set_alerts.png)

## Conclusion

Your AI Evangelist website should now be successfully deployed to Azure Static Web Apps. If you encounter any issues, refer to the troubleshooting section or consult the Azure documentation.

Remember to keep your website content updated and regularly review security best practices to ensure your site remains secure and performs optimally.
