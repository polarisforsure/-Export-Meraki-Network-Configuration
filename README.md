# Meraki Network Configuration Backup

## Overview
This script automates the backup of key network configurations from the **Meraki Dashboard** API. It retrieves and stores:

- VLANs
- Static Routes
- Firewall Rules
- SSID Configurations
- Site-to-Site VPN Settings
- DHCP Settings

All configurations are saved in JSON format for future reference.

## Prerequisites

### 1. Install Python and Required Dependencies
Ensure you have **Python 3.x** installed. Then, install the required Meraki API library:

```bash
pip install meraki
```

### 2. Get Your Meraki API Key
- Go to **Meraki Dashboard** → **Organization** → **Settings**.
- Enable API access if not already enabled.
- Navigate to **My Profile** and generate an **API Key**.

⚠ **Note:** Treat your API Key like a password. Do not share it or expose it in public repositories.

## Usage

### 1. Clone the Repository
```bash
git clone https://github.com/polarisforsure/-Export-Meraki-Network-Configuration.git
cd meraki-config-backup
```

### 2. Configure Your API Key and IDs
Edit `meraki_backup.py` and replace the placeholders:
```python
API_KEY = "YOUR_MERAKI_API_KEY"
ORG_ID = "YOUR_ORG_ID"
NETWORK_ID = "YOUR_NETWORK_ID"
```

To find your **Org ID and Network ID**, run:
```python
from meraki import DashboardAPI

dashboard = DashboardAPI("YOUR_MERAKI_API_KEY", suppress_logging=True)
print(dashboard.organizations.getOrganizations())
```

Then, get the networks in your organization:
```python
print(dashboard.organizations.getOrganizationNetworks(ORG_ID))
```

### 3. Run the Backup Script
Execute the script to retrieve network settings:
```bash
python meraki_backup.py
```

### 4. Check the Output
After running, a new folder `meraki_config_backup/` will be created, containing:
```plaintext
meraki_config_backup/
├── vlans.json
├── static_routes.json
├── firewall_rules.json
├── ssids.json
├── site_to_site_vpn.json
└── dhcp_settings.json
```

## Restoring Configuration
Meraki does **not** support direct import of configurations. However, you can use these JSON files as a reference when manually configuring your new organization.

If needed, an **import script** can be developed to apply these settings programmatically.
