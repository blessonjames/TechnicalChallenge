from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.compute import ComputeManagementClient

class Azure:

    def __init__(self, subscr_id, client_id, tenant_id, secret, resource_group, vm_name):
        self.subscr_id = subscr_id
        self.client_id = client_id
        self.tenant_id = tenant_id
        self.secret = secret
        self.resource_group = resource_group
        self.vm_name = vm_name

    def get_vm_data(self, key):
        try:
            credentials = ServicePrincipalCredentials(client_id=self.client_id,
                                                      secret=self.secret,
                                                      tenant=self.tenant_id)
        except:
            return "Authentication Failed! Invalid Credentials!"
        compute_client = ComputeManagementClient(credentials, self.subscr_id)
        temp_dict = {}
        try:
            virtual_machine = compute_client.virtual_machines.get(self.resource_group, self.vm_name)
        except Exception as e:
            return e            
        temp_dict['vm_name'] = virtual_machine.name
        temp_dict['location'] = virtual_machine.location
        temp_dict['provisioning_state'] = virtual_machine.provisioning_state
        temp_dict['availability_set'] = virtual_machine.availability_set
        temp_dict['id'] = virtual_machine.id
        temp_dict['license_type'] = virtual_machine.license_type
        temp_dict['os_disk_name'] = virtual_machine.storage_profile.os_disk.name
        temp_dict['os_disk_size'] = str(virtual_machine.storage_profile.os_disk.disk_size_gb) + "GB"
        temp_dict['os_type'] = virtual_machine.storage_profile.os_disk.os_type
        if key not in temp_dict.keys():
            return "Unsupported Data Key"
        return temp_dict[key]


def main():

    # Add your azure data in the below variables

    # Service Principal Credentials (For Authentication to Azure)
    subscr_id = ""
    client_id = ""
    tenant_id = ""
    secret = ""

    # VM data
    resource_group = "challenge2-rg"
    vm_name = "testVM2"    

    obj = Azure(subscr_id, client_id, tenant_id, secret, resource_group, vm_name)
    
    # Provide required data key
    # Supported keys: vm_name, location, provisioning_state, availability_set, id, license_type, os_disk_name, os_disk_size, os_type
    data = obj.get_vm_data('os_disk_name')
    print(data)

if __name__ == "__main__":
    main()
    
        
