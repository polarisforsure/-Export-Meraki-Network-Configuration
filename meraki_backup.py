import meraki
import json
import os

# Set your API Key here
API_KEY = "YOUR_MERAKI_API_KEY"

# Initialize the Meraki Dashboard API client
dash = meraki.DashboardAPI(API_KEY, suppress_logging=True)

# Set your organization and network ID (replace these with actual IDs)
ORG_ID = "YOUR_ORG_ID"
NETWORK_ID = "YOUR_NETWORK_ID"

# Create output directory
OUTPUT_DIR = "meraki_config_backup"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def save_to_file(data, filename):
    """Helper function to save JSON data to a file."""
    with open(os.path.join(OUTPUT_DIR, filename), "w") as file:
        json.dump(data, file, indent=4)
    print(f"✅ Saved {filename}")

# Export VLANs
vlans = dash.appliance.getNetworkVlans(NETWORK_ID)
save_to_file(vlans, "vlans.json")

# Export Static Routes
static_routes = dash.appliance.getNetworkApplianceStaticRoutes(NETWORK_ID)
save_to_file(static_routes, "static_routes.json")

# Export Firewall Rules
firewall_rules = dash.appliance.getNetworkApplianceFirewallL3FirewallRules(NETWORK_ID)
save_to_file(firewall_rules, "firewall_rules.json")

# Export SSIDs
ssids = dash.wireless.getNetworkWirelessSsids(NETWORK_ID)
save_to_file(ssids, "ssids.json")

# Export Site-to-Site VPN Config
vpn_settings = dash.appliance.getNetworkApplianceVpnSiteToSiteVpn(NETWORK_ID)
save_to_file(vpn_settings, "site_to_site_vpn.json")

# Export DHCP Settings
dhcp_settings = dash.appliance.getNetworkApplianceDhcpSubnets(NETWORK_ID)
save_to_file(dhcp_settings, "dhcp_settings.json")

print("\n✅ Backup complete! All configurations are saved in the 'meraki_config_backup' folder.")
