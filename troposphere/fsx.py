# Copyright (c) 2019, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
from . import AWSObject, AWSProperty, Tags
from .validators import boolean, integer, storage_type

VALID_LUSTRECONFIGURATION_DEPLOYMENTTYPE = ("PERSISTENT_1", "SCRATCH_1", "SCRATCH_2")


VALID_LUSTRECONFIGURATION_PERUNITSTORAGETHROUGHPUT = (50, 100, 200)


def validate_lustreconfiguration_deploymenttype(
    lustreconfiguration_deploymenttype,
):  # NOQA
    """Validate DeploymentType for LustreConfiguration"""

    if (
        lustreconfiguration_deploymenttype
        not in VALID_LUSTRECONFIGURATION_DEPLOYMENTTYPE
    ):  # NOQA
        raise ValueError(
            "LustreConfiguration DeploymentType must be one of: %s"
            % ", ".join(VALID_LUSTRECONFIGURATION_DEPLOYMENTTYPE)  # NOQA
        )
    return lustreconfiguration_deploymenttype


def validate_lustreconfiguration_perunitstoragethroughput(
    lustreconfiguration_perunitstoragethroughput,
):  # NOQA
    """Validate PerUnitStorageThroughput for LustreConfiguration"""

    if (
        lustreconfiguration_perunitstoragethroughput
        not in VALID_LUSTRECONFIGURATION_PERUNITSTORAGETHROUGHPUT
    ):  # NOQA
        raise ValueError(
            "LustreConfiguration PerUnitStorageThroughput must be one of: %s"
            % ", ".join(VALID_LUSTRECONFIGURATION_PERUNITSTORAGETHROUGHPUT)  # NOQA
        )  # NOQA
    return lustreconfiguration_perunitstoragethroughput


class LustreConfiguration(AWSProperty):
    props = {
        "AutoImportPolicy": (str, False),
        "AutomaticBackupRetentionDays": (integer, False),
        "CopyTagsToBackups": (boolean, False),
        "DailyAutomaticBackupStartTime": (str, False),
        "DataCompressionType": (str, False),
        "DeploymentType": (validate_lustreconfiguration_deploymenttype, False),
        "DriveCacheType": (str, False),
        "ExportPath": (str, False),
        "ImportedFileChunkSize": (integer, False),
        "ImportPath": (str, False),
        "PerUnitStorageThroughput": (
            validate_lustreconfiguration_perunitstoragethroughput,
            False,
        ),  # NOQA
        "WeeklyMaintenanceStartTime": (str, False),
    }


class AuditLogConfiguration(AWSProperty):
    props = {
        "AuditLogDestination": (str, False),
        "FileAccessAuditLogLevel": (str, True),
        "FileShareAccessAuditLogLevel": (str, True),
    }


class SelfManagedActiveDirectoryConfiguration(AWSProperty):
    props = {
        "DnsIps": ([str], False),
        "DomainName": (str, False),
        "FileSystemAdministratorsGroup": (str, False),
        "OrganizationalUnitDistinguishedName": (str, False),
        "Password": (str, False),
        "UserName": (str, False),
    }


class DiskIopsConfiguration(AWSProperty):
    props = {
        "Iops": (integer, False),
        "Mode": (str, False),
    }


class OntapConfiguration(AWSProperty):
    props = {
        "AutomaticBackupRetentionDays": (integer, False),
        "DailyAutomaticBackupStartTime": (str, False),
        "DeploymentType": (str, True),
        "DiskIopsConfiguration": (DiskIopsConfiguration, False),
        "EndpointIpAddressRange": (str, False),
        "FsxAdminPassword": (str, False),
        "PreferredSubnetId": (str, False),
        "RouteTableIds": ([str], False),
        "ThroughputCapacity": (integer, False),
        "WeeklyMaintenanceStartTime": (str, False),
    }


class WindowsConfiguration(AWSProperty):
    props = {
        "ActiveDirectoryId": (str, False),
        "Aliases": ([str], False),
        "AuditLogConfiguration": (AuditLogConfiguration, False),
        "AutomaticBackupRetentionDays": (integer, False),
        "CopyTagsToBackups": (boolean, False),
        "DailyAutomaticBackupStartTime": (str, False),
        "DeploymentType": (str, False),
        "PreferredSubnetId": (str, False),
        "SelfManagedActiveDirectoryConfiguration": (
            SelfManagedActiveDirectoryConfiguration,
            False,
        ),
        "ThroughputCapacity": (integer, True),
        "WeeklyMaintenanceStartTime": (str, False),
    }


class FileSystem(AWSObject):
    resource_type = "AWS::FSx::FileSystem"

    props = {
        "BackupId": (str, False),
        "FileSystemType": (str, True),
        "FileSystemTypeVersion": (str, False),
        "KmsKeyId": (str, False),
        "LustreConfiguration": (LustreConfiguration, False),
        "OntapConfiguration": (OntapConfiguration, False),
        "SecurityGroupIds": ([str], False),
        "StorageCapacity": (integer, False),
        "StorageType": (storage_type, False),
        "SubnetIds": ([str], True),
        "Tags": (Tags, False),
        "WindowsConfiguration": (WindowsConfiguration, False),
    }
