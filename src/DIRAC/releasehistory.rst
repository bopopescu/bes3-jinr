
===============
Version v6r9p25
===============

TS
==

Bugfix
:::::::::::

 - TransformationClient - fixes for processing of derived transformations

Change
:::::::::::

 - TransformationClient - changed default timeout values for service calls


===============
Version v6r9p24
===============

TS
==

Bugfix
:::::::::::

 - TransformationClient - in moveFilesToDerivedTransformation() set file status to Moved-<prod>


===============
Version v6r9p23
===============

Core
====

Bugfix
:::::::::::

 - InstallTools - improper configuration prevents a fresh new installation

WMS
===

Bugfix
:::::::::::

 - PilotDirector - Operations Helper non-instantiated


===============
Version v6r9p22
===============

WMS
===

Bugfix
:::::::::::

 - PilotDirector - allow to properly define extensions to be installed by the Pilot differently to those installed at the server
 - Watchdog - convert pid to string in ProcessMonitor

TS
==

Bugfix
:::::::::::

 - TransformationDB - splitting files in chunks

DMS
===

Change
:::::::::::

 - update dirac-dms-xxx commands to use the new RMS client, strip lines when reading LFNs from a file

Feature
::::::::::::

 - dirac-dms-create-removal-request command


===============
Version v6r9p21
===============

TS
==

Bugfix
:::::::::::

 - Transformation(Client,DB,Manager) - restored FileCatalog compliant interface
 - TransformationDB - fix in __insertIntoExistingTransformationFiles()


===============
Version v6r9p20
===============

Core
====

Bugfix
:::::::::::

 - ProxyUpload - an on the fly upload does not require a proxy to exist

DMS
===

Bugfix
:::::::::::

 - FailoverTransfer - recording the sourceSE in case of failover transfer request

Change
:::::::::::

 - TransferAgent - use compareAdler() for checking checksum

WMS
===

Bugfix
:::::::::::

 - ProcessMonitor - some fixes added, printout when <1 s of consumed CPU is found

Transformation
==============

Bugfix
:::::::::::

 - TransformationClient - fixed return value in moveFilesToDerivedTransformation()

RMS
===

Bugfix
:::::::::::

 - CleanReqDBAgent - now() -> utcnow() in initialize()

Resources
=========

Bugfix
:::::::::::

 - ARCComputingElement - fix the parsing of CE status if no jobs are available


===============
Version v6r9p19
===============

DMS
===

Bugfix
:::::::::::

 - FileCatalog/DirectoryMetadata - inherited metadata is used while selecting directories in findDirIDsByMetadata()


===============
Version v6r9p18
===============

DMS
===

Bugfix
:::::::::::

 - FTSSubmitAgent, FTSRequest - fixes the staging mechanism in the FTS transfer submission

Feature
::::::::::::

 - TransferDBMonitoringHandler - added getFilesForChannel(), resetFileChannelStatus()


===============
Version v6r9p17
===============

Accounting
==========

Bugfix
:::::::::::

 - DataStoreClient - send accounting records in batches of 1000 records instead of 100

DMS:
====

Bugfix
:::::::::::

 - FailoverTransfer - catalog name from list to string
 - FTSSubmitAgent, FTSRequest - handle FTS3 as new protocol and fix bad submission time
 - FTSSubmitAgent, FTSRequest - do not submit FTS transfers for staging files

WMS
===

Bugfix
:::::::::::

 - TaskQueueDB - do not check enabled when TQs are requested from Directors
 - TaskQueueDB - check for Enabled in the TaskQueues when inserting jobs to print an alert

Feature
::::::::::::

 - TaskQueueDB - each TQ can have at most 5k jobs, if beyond the limit create a new TQ to prevent long matching times when there are way too many jobs in a single TQ


===============
Version v6r9p16
===============

TS
==

Bugfix
:::::::::::

 - typos in TransformationCleaningAgent.py

DMS
===

Bugfix
:::::::::::

 - DownloadInputData - try to download only Cached replicas

Change
:::::::::::

 - DownloadInputData - check the available disk space in the right input data directory


===============
Version v6r9p15
===============

Core
====

Bugfix
:::::::::::

 - MySQL - do not decrease the retry counter after ping failure

DMS
===

Bugfix
:::::::::::

 - RemovalTask - fix error string when removing a non existing file (was incompatible with the LHCb BK client).

Change
:::::::::::

 - FC/DirectoryMetadata - Speed up findFilesByMetadataWeb when many files match

WMS
===

Bugfix
:::::::::::

 - JobReport - minor fix ( removed unused imports )
 - JobMonitoring(JobStateUpdate)Handler - jobID argument can be either string, int or long

TS
==

Bugfix
:::::::::::

 - FileReport - minor fix ( inherits object )

Change
:::::::::::

 - TransformationClient - change status of Moved files to a deterministic value


===============
Version v6r9p14
===============

DMS
===

Change
:::::::::::

 - FTSDB - changed schema: removing FTSSite table. From now on FTS sites would be read from CS Resources


===============
Version v6r9p13
===============

FIX: included fixes from v6r8p26 patch release



===============
Version v6r9p12
===============

FIX: included fixes from v6r8p25 patch release



===============
Version v6r9p11
===============

DMS
===

Bugfix
:::::::::::

 - FTSRequest - in __resolveFTSServer() type "=" -> "=="


===============
Version v6r9p10
===============

FIX: included fixes from v6r8p24 patch release


Core
====

Feature
::::::::::::

 - StateMachine utility

DMS
===

Bugfix
:::::::::::

 - in RegisterFile operation handler

Interfaces
==========

Bugfix
:::::::::::

 - Dirac.py - in splitInputData() consider only Active replicas


==============
Version v6r9p9
==============

RMS
===

Bugfix
:::::::::::

 - RequestDB - added getRequestFileStatus(), getRequestName() methods


==============
Version v6r9p8
==============

DMS
===

Bugfix
:::::::::::

 - RequestDB - get correct digest ( short request description ) of a request


==============
Version v6r9p7
==============

FIX: included fixes from v6r8p23 patch release


RSS
===

Bugfix
:::::::::::

 - SpaceTokenOccupancyPolicy - SpaceToken Policy decision was based on percentage by mistake

RMS
===

Bugfix
:::::::::::

 - FTSAgent - setting space tokens for newly created FTSJobs

Feature
::::::::::::

 - new scripts dirac-dms-ftsdb-summary, dirac-dms-show-ftsjobs


==============
Version v6r9p6
==============

DMS
===

Bugfix
:::::::::::

 - dirac-admin-add-ftssite - missing import

RMS
===

Feature
::::::::::::

 - RequestDB, ReqManagerHandler - added getRequestStatus() method

TS
==

Bugfix
:::::::::::

 - fixes when using new RequestClient with the TransformationCleaningAgent

WMS
===

Bugfix
:::::::::::

 - typo in SandboxStoreHandler transfer_fromClient() method


==============
Version v6r9p5
==============

DMS
===

Bugfix
:::::::::::

 - missing proxy in service env in the FTSManager service. By default service will use DataManager proxy refreshed every 6 hours.

Resources
=========

Feature
::::::::::::

 - StorageElement - new checkAccess policy: split the self.checkMethods in self.okMethods. okMethods are the methods that do not use the physical SE. The isValid returns S_OK for all those immediately

RSS
===

Bugfix
:::::::::::

 - SpaceTokenOccupancyPolicy - Policy that now takes into account absolute values for the space left

TS
==

Bugfix
:::::::::::

 - TransformationCleaningAgent - will look for both old and new RMS


==============
Version v6r9p4
==============

Stager
======

Feature
::::::::::::

 - Stager API: dirac-stager-monitor-file, dirac-stager-monitor-jobs, dirac-stager-monitor-requests, dirac-stager-show-stats


==============
Version v6r9p3
==============

Transformation
==============

Bugfix
:::::::::::

 - TransformationCleaning Agent status was set to 'Deleted' instead of 'Cleaned'


==============
Version v6r9p2
==============

RSS
===

Bugfix
:::::::::::

 - removed old & unused code

Feature
::::::::::::

 - Added Component family tables and statuses
 - allow RSS policies match wild cards on CS

WMS
===

Bugfix
:::::::::::

 - FailoverTransfer,JobWrapper - proper propagation of file metadata


==============
Version v6r9p1
==============

RMS
===

Change
:::::::::::

 - FTSJob - add staging flag in in submitFTS2
 - Changes in WMS (FailoverTransfer, JobReport, JobWrapper, SandboxStoreHandler) and TS (FileReport) to follow the new RMS.

Feature
::::::::::::

 - FTSAgent - update rwAccessValidStamp, update ftsGraphValidStamp, new option for staging files before submission, better log handling here and there
 - Full CRUD support in RMS.

RSS
===

Feature
::::::::::::

 - ResourceManagementDB - new table ErrorReportBuffer
 - new ResourceManagementClient methods - insertErrorReportBuffer, selectErrorReportBuffer, deleteErrorReportBuffer


============
Version v6r9
============

NEW: Refactored Request Management System, related DMS agents and FTS management

     components



===============
Version v6r8p28
===============

Core
====

Bugfix
:::::::::::

 - RequestHandler - the lock Name includes ActionType/Action

DMS
===

Bugfix
:::::::::::

 - dirac-dms-filecatalog-cli - prevent exception in case of missing proxy


===============
Version v6r8p27
===============

DMS
===

Bugfix
:::::::::::

 - dirac-dms-add-file - fixed typo item -> items


===============
Version v6r8p26
===============

Core
====

Feature
::::::::::::

 - RequestHandler - added getServiceOption() to properly resolve inherited options in the global service handler initialize method
 - FileCatalogHandler, StorageElementHandler - use getServiceOption()


===============
Version v6r8p25
===============

FIX: included fixes from v6r7p40 patch release


Resources
=========

Bugfix
:::::::::::

 - SRM2Storage - do not account gfal_ls operations


===============
Version v6r8p24
===============

FIX: included fixes from v6r7p39 patch release


Core
====

Bugfix
:::::::::::

 - SiteSEMapping was returning wrong info

DMS
===

Bugfix
:::::::::::

 - FTSRequest - choose explicitly target FTS point for RAL and CERN
 - StrategyHandler - wrong return value in __getRWAccessForSE()

Resources
=========

Change
:::::::::::

 - SRM2Storage - do not account gfal_ls operations any more


===============
Version v6r8p23
===============

FIX: included fixes from v6r7p37 patch release


TS
==

Bugfix
:::::::::::

 - TransformationDB - allow tasks made with ProbInFC files
 - TransformationCleaingAgent,Client - correct setting of transformation status while cleaning


===============
Version v6r8p22
===============

FIX: included fixes from v6r7p36 patch release



===============
Version v6r8p21
===============

DMS
===

Bugfix
:::::::::::

 - FileCatalog/DirectoryMetadata - even if there is no meta Selection the path should be considered when getting Compatible Metadata
 - FileCatalog/DirectoryNodeTree - findDir will return S_OK( '' ) if dir not found, always return the same error from DirectoryMetadata in this case.

RSS
===

Bugfix
:::::::::::

 - DowntimeCommand - use UTC time stamps

TS
==

Bugfix
:::::::::::

 - TransformationAgent - in _getTransformationFiles() get also ProbInFC files in addition to Used


===============
Version v6r8p20
===============

Stager
======

Feature
::::::::::::

 - Stager API: dirac-stager-monitor-file, dirac-stager-monitor-jobs, dirac-stager-monitor-requests, dirac-stager-show-stats


===============
Version v6r8p19
===============

Transformation
==============

Bugfix
:::::::::::

 - TransformationCleaning Agent status was set to 'Deleted' instead of 'Cleaned'


===============
Version v6r8p18
===============

TS
==

Bugfix
:::::::::::

 - TransformationAgent - regression in __cleanCache()


===============
Version v6r8p17
===============

FIX: included fixes from v6r7p32 patch release


WMS
===

Bugfix
:::::::::::

 - StalledJobAgent - for accidentally stopped jobs ExecTime can be not set, set it to CPUTime for the accounting purposes in this case


===============
Version v6r8p16
===============

FIX: included fixes from v6r7p31 patch release


WMS
===

Bugfix
:::::::::::

 - TaskQueueDB - fixed a bug in the negative matching conditions SQL construction

RSS
===

Bugfix
:::::::::::

 - Minor changes to ensure consistency if ElementInspectorAgent and users interact simultaneously with the same element
 - SummarizeLogsAgent - the logic of the agent was wrong, the agent has been re-written.

Change
:::::::::::

 - removed DatabaseCleanerAgent ( to be uninstalled if already installed )

Feature
::::::::::::

 - improved doc strings of PEP, PDP modules ( part of PolicySystem )


===============
Version v6r8p15
===============

Core
====

Bugfix
:::::::::::

 - X509Chain - fix invalid information when doing dirac-proxy-info without CS ( in getCredentials() )

RSS
===

Feature
::::::::::::

 - PDP, PEP - added support for option "doNotCombineResult" on PDP


===============
Version v6r8p14
===============

Core
====

Bugfix
:::::::::::

 - dirac-deploy-scripts - can now work with the system python

WMS
===

Bugfix
:::::::::::

 - Executor/InputData - Add extra check for LFns in InputData optimizer, closes #1472

Feature
::::::::::::

 - dirac-wms-cpu-normalization - added -R option to modify a given configuration file

Transformation
==============

Bugfix
:::::::::::

 - TransformationAgent - bug in __cleanCache() dict modified in a loop

Change
:::::::::::

 - TransformationAgent - add possibility to kick a transformation (not skip it if no unused files), by touching a file in workDirectory


===============
Version v6r8p13
===============

Transformation
==============

Bugfix
:::::::::::

 - TransformationDB - restored import of StringType


===============
Version v6r8p12
===============

NEW: Applied patches from v6r7p29


WMS
===

Bugfix
:::::::::::

 - JobDB - check if SystemConfig is present in the job definition and convert it into Platform

DMS
===

Bugfix
:::::::::::

 - ReplicaManager - do not get metadata of files when getting files in a directory if not strictly necessary

RSS
===

Feature
::::::::::::

 - ported from LHCb PublisherHandler for RSS web views


===============
Version v6r8p11
===============

NEW: Applied patches from v6r7p27


RSS
===

Feature
::::::::::::

 - SpaceTokenOccupancyPolicy - ported from LHCbDIRAC
 - db._checkTable done on service initialization ( removed dirac-rss-setup script doing it )

Transformation
==============

Bugfix
:::::::::::

 - TaskManager - reset oJob for each task in prepareTransformationTasks()
 - ValidateOutputDataAgent - typo fixed in getTransformationDirectories()
 - TransformationManagerHandler - use CS to get files statuses not to include in processed file fraction calculation for the web monitoring pages


===============
Version v6r8p10
===============

NEW: Applied patches from v6r7p27



==============
Version v6r8p9
==============

DMS
===

Bugfix
:::::::::::

 - TransferAgent,dirac-dms-show-se-status, ResourceStatus,TaskManager - fixes needed for DMS components to use RSS status information

Feature
::::::::::::

 - ReplicaManager - allow to get metadata for an LFN+SE as well as PFN+SE


==============
Version v6r8p8
==============

RSS
===

Bugfix
:::::::::::

 - dirac-rss-setup - added missing return of S_OK() result


==============
Version v6r8p7
==============

NEW: Applied patches from v6r7p24


DMS
===

Bugfix
:::::::::::

 - LcgFileCatalogClient - bug in addFile()

RSS
===

Bugfix
:::::::::::

 - fixed script dirac-rss-set-token, broken in the current release.

Feature
::::::::::::

 - Statistics module - will be used in the future to provide detailed information from the History of the elements


==============
Version v6r8p6
==============

NEW: Applied patches from v6r7p23


Transformation
==============

Bugfix
:::::::::::

 - TaskManager - allow prepareTransformationTasks to proceed if no OutputDataModule is defined
 - TransformationDB - remove INDEX(TaskID) from TransformationTasks. It produces a single counter for the whole table instead of one per TransformationID

WMS
===

Bugfix
:::::::::::

 - WMSUtilities - to allow support for EMI UI's for pilot submission we drop support for glite 3.1


==============
Version v6r8p5
==============

NEW: Applied patches from v6r7p22


RSS
===

Change
:::::::::::

 - removed old tests and commented out files

WMS
===

Bugfix
:::::::::::

 - PoolXMLCatalog - proper addFile usage

Transformation
==============

Change
:::::::::::

 - TransformationAgent - clear replica cache when flushing or setting a file in the workdirectory


==============
Version v6r8p4
==============

Transformation
==============

Bugfix
:::::::::::

 - The connection to the jobManager is done only at submission time
 - Jenkins complaints fixes

WMS
===

Bugfix
:::::::::::

 - JobDB - CPUtime -> CPUTime
 - Jenkins complaints fixes


==============
Version v6r8p3
==============

DMS
===

Bugfix
:::::::::::

 - LcgFileCatalogClient


==============
Version v6r8p2
==============

DMS:
====

Bugfix
:::::::::::

 - LcgFileCatalogClient - remove check for opening a session in __init__ as credentials are not yet set

Transformation
==============

Change
:::::::::::

 - reuse RPC clients in Transformation System


==============
Version v6r8p1
==============

Core
====

Bugfix
:::::::::::

 - dirac-deploy-scripts - restored regression w.r.t. support of scripts starting with "d"

DMS
===

Bugfix
:::::::::::

 - LcgFileCatalogClient - two typos fixed


============
Version v6r8
============

CHANGE: Several fixes backported from the v7r0 integration branch


Core
====

Bugfix
:::::::::::

 - X509Chain - proxy-info showing an error when there's no CS

Change
:::::::::::

 - DictCache - uses global LockRing to avoid locks in multiprocessing

DMS
===

Bugfix
:::::::::::

 - TransferAgent - inside loop filter out waiting files dictionary
 - dirac-admin-allow-se - there was a continue that was skipping the complete loop for ARCHIVE elements

Feature
::::::::::::

 - LcgFileCatalogClient - test return code in startsess lfc calls

WMS:
====

Bugfix
:::::::::::

 - OptimizerExecutor, InputData, JobScheduling - check that site candidates have all the replicas

RSS:
====

Bugfix
:::::::::::

 - ResourceStatus, RSSCacheNoThread - ensure that locks are always released

Transformation
==============

Bugfix
:::::::::::

 - TaskManager - site in the job definition is taken into account when submitting
 - ValidateOutputDataAgent - self not needed for static methods

Feature
::::::::::::

 - Transformation - get the allowed plugins from the CS /Operations/Transformations/AllowedPlugins


===============
Version v6r7p40
===============

Resources
=========

Bugfix
:::::::::::

 - StorageElement class was not properly passing the lifetime argument for prestageFile method


===============
Version v6r7p39
===============

Core
====

Change
:::::::::::

 - Grid - in executeGridCommand() allow environment script with arguments needed for ARC client

DMS
===

Bugfix
:::::::::::

 - DFC SEManager - DIP Storage can have a list of ports now

Resources
=========

Bugfix
:::::::::::

 - ARCComputingElement - few fixes after debugging


===============
Version v6r7p38
===============

Core
====

Feature
::::::::::::

 - DISET FileHelper, TransferClient - possibility to switch off check sum

Resources
=========

Bugfix
:::::::::::

 - SSHComputingElement - use CE name in the pilot reference construction

Feature
::::::::::::

 - ARCComputingElement - first version
 - StorageFactory - possibility to pass extra protocol parameters to storage object
 - DIPStorage - added CheckSum configuration option

WMS
===

Bugfix
:::::::::::

 - StalledJobAgent - if ExecTime < CPUTime make it equal to CPUTime


===============
Version v6r7p37
===============

Framework
=========

Bugfix
:::::::::::

 - NotificationDB - typos in SQL statement in purgeExpiredNotifications()

WMS
===

Change
:::::::::::

 - JobWrapper - report only error code as ApplicationError parameter when payload finishes with errors

Feature
::::::::::::

 - JobCleaningAgent - added scheduling sandbox LFN removal request when deleting jobs
 - SiteDirector - possibility to specify extensions to be installed in pilots in /Operations/Pilots/Extensions option in order not to install all the server side extensions

DMS
===

Change
:::::::::::

 - FileCatalogFactory - use service path as default URL
 - FileCatalogFactory - use ObjectLoader to import catalog clients

SMS
===

Bugfix
:::::::::::

 - StorageManagementDB, dirac-stager-monitor-jobs - small bug fixes ( sic, Daniela )

Resources
=========

Bugfix
:::::::::::

 - StalledJobAgent - if pilot reference is not registered, this is not an error of the StalledJobAgent, no log.error() in  this case

Change
:::::::::::

 - DIPStorage - added possibility to specify a list of ports for multiple service end-points
 - InProcessComputingElement - demote log message when payload failure to warning, the job will fail anyway

RMS
===

Change
:::::::::::

 - RequestTask - ensure that tasks are executed with user credentials even with respect to queries to DIRAC services ( useServerCertificate flag set to false )


===============
Version v6r7p36
===============

WMS
===

Bugfix
:::::::::::

 - CREAMCE, SiteDirector - make sure that the tmp executable is removed

Change
:::::::::::

 - JobWrapper - remove sending mails via Notification Service in case of job rescheduling

SMS
===

Bugfix
:::::::::::

 - StorageManagementDB - fix a race condition when old tasks are set failed between stage submission and update.


===============
Version v6r7p35
===============

Stager
======

Feature
::::::::::::

 - Stager API: dirac-stager-monitor-file, dirac-stager-monitor-jobs, dirac-stager-monitor-requests, dirac-stager-show-stats


===============
Version v6r7p34
===============

Transformation
==============

Bugfix
:::::::::::

 - TransformationCleaning Agent status was set to 'Deleted' instead of 'Cleaned'


===============
Version v6r7p33
===============

Interfaces
==========

Bugfix
:::::::::::

 - Job.py - in setExecutable() - prevent changing the log file name string type

StorageManagement
=================

Bugfix
:::::::::::

 - StorageManagementDB - demote the level of several log messages

Feature
::::::::::::

 - StorageManagementDB(Handler) - kill staging requests at the same time as killing related jobs, closes #1510


===============
Version v6r7p32
===============

DMS
===

Bugfix
:::::::::::

 - StorageElementHandler - do not use getDiskSpace utility, use os.statvfs instead

Change
:::::::::::

 - StorageManagementDB - in getStageRequests() make MySQL do an UNIQUE selection and use implicit loop to speed up queries for large results

Resources
=========

Bugfix
:::::::::::

 - lsfce remote script - use re.search instead of re.match in submitJob() to cope with multipline output


===============
Version v6r7p31
===============

WMS
===

Bugfix
:::::::::::

 - SiteDirector - make possible more than one SiteDirector (with different pilot identity) attached to a CE, ie sgm and pilot roles. Otherwise one is declaring Aborted the pilots from the other.


===============
Version v6r7p30
===============

Core
====

Bugfix
:::::::::::

 - InstallTools - in getSetupComponents() typo fixed: agent -> executor

Change
:::::::::::

 - X509Chain - added groupProperties field to the getCredentials() report


===============
Version v6r7p29
===============

DMS
===

Bugfix
:::::::::::

 - dirac-dms-fts-monitor - exit with code -1 in case of error

Change
:::::::::::

 - FileCatalog - selection metadata is also returned as compatible metadata in the result of getCompatibleMetadata() call

Feature
::::::::::::

 - FileCatalog - added path argument to getCompatibleMetadata() call
 - FileCatalogClient - added getFileUserMetadata()

Resources
=========

Bugfix
:::::::::::

 - CREAMComputingElement - check globus-url-copy result for errors when retrieving job output


===============
Version v6r7p28
===============

DMS
===

Bugfix
:::::::::::

 - FileCatalog/DirectoryMetadata - wrong MySQL syntax


===============
Version v6r7p27
===============

Core
====

Bugfix
:::::::::::

 - Mail.py - fix of the problem of colons in the mail's body

Interfaces
==========

Feature
::::::::::::

 - Job API - added setSubmitPools(), setPlatform() sets ... "Platform"

WMS
===

Bugfix
:::::::::::

 - TaskQueueDB - use SystemConfig as Platform for matching ( if Platform is not set explicitly

Resources
=========

Bugfix
:::::::::::

 - SSHComputingElement - use ssh host ( and not CE name ) in the pilot reference
 - SSHGEComputingElement - forgotten return statement in _getJobOutputFiles()

Framework
=========

Feature
::::::::::::

 - dirac-sys-sendmail - email's body can be taken from pipe. Command's argument in this case will be interpreted as a destination address


===============
Version v6r7p26
===============

DMS
===

Bugfix
:::::::::::

 - ReplicaManager - status names Read/Write -> ReadAccess/WriteAccess


===============
Version v6r7p25
===============

Core
====

Change
:::::::::::

 - X509Chain - in getCredentials() failure to contact CS is not fatal, can happen when calling dirac-proxy-init -x, for example


===============
Version v6r7p24
===============

DMS
===

Feature
::::::::::::

 - FileCatalog - added getFilesByMetadataWeb() to allow pagination in the Web catalog browser

WMS
===

Change
:::::::::::

 - WMSAdministrator, DiracAdmin - get banned sites list by specifying the status to the respective jobDB call


===============
Version v6r7p23
===============

Transformation
==============

Bugfix
:::::::::::

 - TransformationDB - badly formatted error log message

RMS
===

Change
:::::::::::

 - RequestDBMySQL - speedup the lookup of requests

WMS
===

Bugfix
:::::::::::

 - dirac-dms-job-delete - in job selection by group

DMS
===

Bugfix
:::::::::::

 - LcgFileCatalogClient - getDirectorySize made compatible with DFC
 - LcgFileCatalogClient - proper call of __getClientCertInfo()


===============
Version v6r7p22
===============

Transformation
==============

Change
:::::::::::

 - InputDataAgent - treats only suitable transformations, e.g. not the extendable ones.
 - TransformationAgent - make some methods more public for easy overload


===============
Version v6r7p21
===============

Core
====

Bugfix
:::::::::::

 - Shifter - pass filePath argument when downloading proxy


===============
Version v6r7p20
===============

DMS
===

Bugfix
:::::::::::

 - StorageElement, SRM2Storage - support for '*Access' statuses, checking results of return structures

Change
:::::::::::

 - StrategyHandler - move out SourceSE checking to TransferAgent
 - ReplicaManager, InputDataAgent - get active replicas

RSS
===

Bugfix
:::::::::::

 - Synchronizer - moved to ResourceManager handler

Feature
::::::::::::

 - set configurable email address on the CS to send the RSS emails
 - RSSCache without thread in background


===============
Version v6r7p19
===============

DMS
===

Bugfix
:::::::::::

 - ReplicaManager - in putAndRegister() SE.putFile() singleFile argument not used explicitly


===============
Version v6r7p18
===============

WMS
===

Bugfix
:::::::::::

 - StalledJobAgent - do not exit the loop over Completed jobs if accounting sending fails
 - JobManifest - If CPUTime is not set, set it to MaxCPUTime value

Feature
::::::::::::

 - dirac-wms-job-delete - allow to specify jobs to delete by job group and/or in a file


===============
Version v6r7p17
===============

Resources
=========

Bugfix
:::::::::::

 - SRM2Storage - treat properly "22 SRM_REQUEST_QUEUED" result code


===============
Version v6r7p16
===============

DMS
===

Bugfix
:::::::::::

 - StrategyHandler - do not proceed when the source SE is not valid for read
 - StorageElement - putFile can take an optional sourceSize argument
 - ReplicaManager - in removeFile() proper loop on failed replicas

RSS
===

Bugfix
:::::::::::

 - SpaceTokenOccupancyCommand, CacheFeederAgent - add timeout when calling lcg_util commands

WMS
===

Bugfix
:::::::::::

 - JobManifest - take all the SubmitPools defined in the TaskQueueAgent

Feature
::::::::::::

 - StalledJobAgent - declare jobs stuck in Completed status as Failed


===============
Version v6r7p15
===============

Core
====

Bugfix
:::::::::::

 - SocketInfo - in host identity evaluation

DMS
===

Bugfix
:::::::::::

 - FileCatalogHandler - missing import os

Transformation
==============

Change
:::::::::::

 - JobManifest - getting allowed job types from operations() section


===============
Version v6r7p14
===============

DMS
===

Bugfix
:::::::::::

 - StorageElementProxy - free the getFile space before the next file
 - StorageElement - added getPFNBase() to comply with the interface

Change
:::::::::::

 - StorageElementProxy - removed getParameters(), closes #1280

Interfaces
==========

Change
:::::::::::

 - Dirac API - allow lists of LFNs in removeFile() and removeReplica()

WMS
===

Change
:::::::::::

 - JobSchedulingAgent(Executor) - allow both BannedSite and BannedSites JDL option

RSS
===

Bugfix
:::::::::::

 - ElementInspectorAgent - should only pick elements with rss token ( rs_svc ).
 - TokenAgent - using 4th element instead of the 5th. Added option to set admin email on the CS.


===============
Version v6r7p13
===============

Core
====

Bugfix
:::::::::::

 - Resources - in getStorageElementSiteMapping() return only sites with non-empty list of SEs

DMS
===

Bugfix
:::::::::::

 - StorageElement - restored the dropped logic of using proxy SEs
 - FileCatalog - fix the UseProxy /LocalSite/Catalog option

Transformation
==============

Bugfix
:::::::::::

 - TransformationDB - use lower() string comparison in extendTransformation()


===============
Version v6r7p12
===============

WMS
===

Bugfix
:::::::::::

 - JobManifest - get AllowedSubmitPools from the /Systems section, not from /Operations

Core
====

Feature
::::::::::::

 - Resources helper - added getSites(), getStorageElementSiteMapping()

DMS
===

Bugfix
:::::::::::

 - ReplicaManager - do not modify the loop dictionary inside the loop

Change
:::::::::::

 - StrategyHandler - use getStorageElementSiteMapping helper function


===============
Version v6r7p11
===============

Core
====

Change
:::::::::::

 - Subprocess - put the use of watchdog in flagging


===============
Version v6r7p10
===============

Core
====

Bugfix
:::::::::::

 - Subprocess - returns correct structure in case of timeout, closes #1295, #1294
 - Logger - cleaned unused imports

Change
:::::::::::

 - TimeOutExec - dropped unused utility

Feature
::::::::::::

 - Logger - added getLevel() method, closes #1292

RSS
===

Change
:::::::::::

 - ElementInspectorAgent - do not use mangled name and removed shifterProxy agentOption


==============
Version v6r7p9
==============

Core
====

Bugfix
:::::::::::

 - InstallTools - MySQL Port should be an integer


==============
Version v6r7p8
==============

Core
====

Bugfix
:::::::::::

 - Subprocess - consistent timeout error message

DMS
===

Bugfix
:::::::::::

 - StrategyHandler - check file source CEs

Change
:::::::::::

 - DataIntegrityClient - code beautification
 - ReplicaManager - do not check file existence if replica information is queried anyway, do not fail if file to be removed does not exist already.

Feature
::::::::::::

 - RemovalTask - added bulk removal


==============
Version v6r7p7
==============

FIX: Several fixes to allow automatic code documentation


Core
====

Feature
::::::::::::

 - InstallTools - added mysqlPort and mysqlRootUser

DMS
===

Change
:::::::::::

 - ReplicaManager - set possibility to force the deletion of non existing files
 - StrategyHandler - better handling of checksum check during scheduling


==============
Version v6r7p6
==============

Core
====

Bugfix
:::::::::::

 - dirac-install - restore signal alarm if downloadable file is not found
 - Subprocess - using Manager proxy object to pass results from the working process

DMS:
====

Bugfix
:::::::::::

 - FTSMonitorAgent, TransferAgent - fix the names of the RSS states

Change
:::::::::::

 - StorageElement - removed overwride mode
 - removed obsoleted dirac-dms-remove-lfn-replica, dirac-dms-remove-lfn

Feature
::::::::::::

 - FTSMonitorAgent - filter out sources with checksum mismatch

RSS
===

Feature
::::::::::::

 - ElementInspectorAgent runs with a variable number of threads which are automatically adjusted
 - Added policies to force a particular state, can be very convenient to keep something Banned for example.
 - policy system upgrade, added finer granularity when setting policies and actions

WMS
===

Change
:::::::::::

 - JobDescription, JobManifest - take values for job parameter verification from Operations CS section

Feature
::::::::::::

 - SiteDirector- allow to define pilot DN/Group in the agent options


==============
Version v6r7p5
==============

Interfaces
==========

Bugfix
:::::::::::

 - dirac-wms-job-get-output - properly treat the case when output directory is not specified


==============
Version v6r7p4
==============

Core
====

Bugfix
:::::::::::

 - Subprocess - avoid that watchdog kills the executor process before it returns itself

Framework
=========

Bugfix
:::::::::::

 - ProxuManagerClient - wrong time for caching proxies

RSS
===

Bugfix
:::::::::::

 - removed obsoleted methods

DMS
===

Feature
::::::::::::

 - FileCatalog - added findFilesByMetadataDetailed - provides detailed metadata for selected files


==============
Version v6r7p3
==============

DMS
===

Bugfix
:::::::::::

 - FTSMonitorAgent - logging less verbose

Transformation
==============

Bugfix
:::::::::::

 - TransformationAgent - use the new CS defaults locations
 - Proper agent initialization

Feature
::::::::::::

 - TransformationPlaugin - in Broadcast plugin added file groupings by number of files, make the TargetSE always defined, even if the SourceSE list contains it

ResourceStatus
==============

Bugfix
:::::::::::

 - Added the shifter's proxy to several agents

RMS
===

Bugfix
:::::::::::

 - RequestContainer - the execution order was not properly set for the single files

Framework:
==========

Bugfix
:::::::::::

 - ProxyManagerClient - proxy time can not be shorter than what was requested


==============
Version v6r7p2
==============

Core
====

Bugfix
:::::::::::

 - dirac-configure - switch to use CS before checking proxy info

Framework
=========

Feature
::::::::::::

 - dirac-sys-sendmail new command
 - SystemAdmininistratorCLI - added show host, uninstall, revert commands
 - SystemAdmininistratorHandler - added more info in getHostInfo()
 - SystemAdmininistratorHandler - added revertSoftware() interface

Transformation
==============

Bugfix
:::::::::::

 - TransformationCleaningAgent - check the status of returned results


==============
Version v6r7p1
==============

Core
====

Bugfix
:::::::::::

 - Subprocess - finalize the Watchdog closing internal connections after a command execution

Change
:::::::::::

 - add timeout for py(shell,system)Call calls where appropriate
 - Shifter - use gProxyManager in a way that allows proxy caching

Framework
=========

Bugfix
:::::::::::

 - ProxyDB - replace instead of delete+insert proxy in __storeVOMSProxy

Feature
::::::::::::

 - ProxyManagerClient - allow to specify validity and caching time separately

DMS
===

Bugfix
:::::::::::

 - dirac-dms-add-file - allow LFN: prefix for lfn argument

Feature
::::::::::::

 - FTSMonitorAgent - made multithreaded for better efficiency

WMS
===

Bugfix
:::::::::::

 - TaskQueueDB - fixed selection SQL in __generateTQMatchSQL()

Change
:::::::::::

 - OptimizerExecutor - reduce diversity of MinorStatuses for failed executors

Feature
::::::::::::

 - dirac-wms-job-get-output, dirac-wms-job-status - allow to retrieve output for a job group

Resources
=========

Bugfix
:::::::::::

 - CREAMComputingElement - remove temporary JDL right after the submission


===============
Version v6r6p21
===============

DMS
===

Bugfix
:::::::::::

 - TransformationCleaningAgent - use the right signature of cleanMetadataCatalogFiles() call


===============
Version v6r6p20
===============

DMS
===

Bugfix
:::::::::::

 - RegistrationTask - properly escaped error messages
 - DirectoryMetadata - use getFileMetadataFields from FileMetadata in addMetadataField()

Feature
::::::::::::

 - When there is a missing source error spotted during FTS transfer, file should be reset and rescheduled again until maxAttempt (set to 100) is reached

WMS
===

Bugfix
:::::::::::

 - JobScheduling - fix the site group logic in case of Tier0


===============
Version v6r6p19
===============

DMS
===

Bugfix
:::::::::::

 - All DMS agents  - set up agent name in the initialization

Core
====

Bugfix
:::::::::::

 - Time - proper interpreting of 0's instead of None
 - Os.py - protection against failed "df" command execution

Change
:::::::::::

 - DISET - use cStringIO for ANY read that's longer than 16k (speed improvement) + Less mem when writing data to the net
 - PlotBase - made a new style class

Feature
::::::::::::

 - Subprocess - timeout wrapper for subprocess calls
 - dirac-info prints lcg bindings versions
 - Subprocess - added debug level log message

Framework
=========

Bugfix
:::::::::::

 - dirac-proxy-init - always check for errors in S_OK/ERROR returned structures

Change
:::::::::::

 - Do not accept VOMS proxies when uploading a proxy to the proxy manager

Feature
::::::::::::

 - SystemAdministratorIntegrator client for collecting info from several hosts
 - SystemAdministrator - added getHostInfo()

Configuration
=============

Bugfix
:::::::::::

 - CE2CSAgent - get a fresh copy of the cs data before attempting to modify it, closes #1151
 - Do not create useless backups due to slaves connecting and disconnecting
 - Refresher - prevent retrying with 'Insane environment'

Accounting
==========

Bugfix
:::::::::::

 - DBUtils - take into account invalid values, closes #949

Feature
::::::::::::

 - Accounting/Job - added validation of reported values to cope with the weird Yandex case

DMS
===

Bugfix
:::::::::::

 - FTSSubmitAgent - file for some reason rejected from submission should stay in 'Waiting' in TransferDB.Channel table
 - FTSRequest - fix in the log printout
 - FileCatalogCLI - check the result of removeFile call
 - LcgFileCatalogClient - get rid of LHCb specific VO evaluation
 - Restored StorageElementProxy functionality

Change
:::::::::::

 - dirac-dms-add-file removed, dirac-dms-add-files renamed to dirac-dms-add-file
 - dirac-dms-add-file - added printout

Feature
::::::::::::

 - New FileCatalogProxy service - a generalization of a deprecated LcgFileCatalog service
 - FileCatalog(Factory), StorageElement(Factory) - UseProxy flag moved to /Operations and /LocalSite sections

RSS
===

Bugfix
:::::::::::

 - dirac-admin-allow/ban-se - allow a SE on Degraded ( Degraded->Active ) and ban a SE on Probing ( Probing -> Banned ). In practice, Active and Degraded are "usable" states anyway.

Feature
::::::::::::

 - general reimplementation: New DB schema using python definition of tables, having three big blocks: Site, Resource and Node. MySQLMonkey functionality almost fully covered by DB module, eventually will disappear. Services updated to use new database. Clients updated to use new database. Synchronizer updated to fill the new database. When helpers will be ready, it will need an update. One ElementInspectorAgent, configurable now is hardcoded. New Generic StateMachine using OOP. Commands and Policies simplified. ResourceStatus using internal cache, needs to be tested with real load. Fixes for the state machine Replaced Bad with Degraded status ( outside RSS ). Added "Access" to Read|Write|Check|Remove SE statuses wherever it applies. ResourceStatus returns by default "Active" instead of "Allowed" for CS calls. Caching parameters are defined in the CS

WMS
===

Bugfix
:::::::::::

 - OptimizerExecutor - failed optimizations will still update the job
 - JobWrapper - do not attempt to untar directories before having checked if they are tarfiles

Change
:::::::::::

 - JobDB - do not interpret SystemConfig in the WMS/JobDB
 - JobDB - Use CPUTime JDL only, keep MaxCPUTime for backward compatibility
 - JobWrapper - use CPUTime job parameter instead of MaxCPUTime
 - JobAgent - use CEType option instead of CEUniqueID

Feature
::::::::::::

 - JobWrapper - added LFNUserPrefix VO specific Operations option used for building user LFNs
 - dirac-wms-job-status - get job statuses for jobs in a given job group

SMS
===

Bugfix
:::::::::::

 - StorageManagementDB - when removing unlinked replicas, take into account the case where a staging request had been submitted, but failed

Resources
=========

Feature
::::::::::::

 - glexecCE - add new possible locations of the glexec binary: OSG specific stuff and in last resort looking in the PATH
 - LcgFileCatalogClient - in removeReplica() get the needed PFN inside instead of providing it as an argument

TS
==

Change
:::::::::::

 - Transformation types definition are moved to the Operations CS section

Interfaces
==========

Bugfix
:::::::::::

 - Dirac.py - CS option Scratchdir was in LocalSite/LocalSite
 - Dirac.py - do not define default catalog, use FileCatalog utility instead


===============
Version v6r6p19
===============

DMS
===

Bugfix
:::::::::::

 - All DMS agents  - set up agent name in the initialization


===============
Version v6r6p18
===============

Transformation
==============

Change
:::::::::::

 - /DIRAC/VOPolicy/OutputDataModule option moved to <Operations>/Transformations/OutputDataModule

Resources
=========

Bugfix
:::::::::::

 - ComputingElement - properly check if the pilot proxy has VOMS before adding it to the payload when updating it

WMS
===

Bugfix
:::::::::::

 - JobSanity - fixed misspelled method call SetParam -> SetParameter


===============
Version v6r6p17
===============

Transformation
==============

Bugfix
:::::::::::

 - TransformationAgent - corrected  __getDataReplicasRM()


===============
Version v6r6p16
===============

DMS
===

Bugfix
:::::::::::

 - Agents - proper __init__ implementation with arguments passing to the super class
 - LcgFileCatalogClient - in removeReplica() reload PFN in case it has changed


===============
Version v6r6p15
===============

Framework
=========

Bugfix
:::::::::::

 - ErrorMessageMonitor - corrected updateFields call

DMS:
====

Feature
::::::::::::

 - FTSMonitorAgent completely rewritten in a multithreaded way

Transformation
==============

Bugfix
:::::::::::

 - InputDataAgent - proper instantiation of TransformationClient

Change
:::::::::::

 - Transformation - several log message promoted from info to notice level


===============
Version v6r6p14
===============

Transformation
==============

Bugfix
:::::::::::

 - Correct instantiation of agents inside several scripts
 - TransformationAgent - return an entry for all LFNs in __getDataReplicasRM

Change
:::::::::::

 - TransformationCleaningAgent - added verbosity to logs
 - TransformationAgent - missingLFC to MissingInFC as it could be the DFC as well

DMS
===

Bugfix
:::::::::::

 - TransferAgent - fix exception reason in registerFiles()


===============
Version v6r6p13
===============

DMS
===

Change
:::::::::::

 - TransferAgent - change RM call from getCatalogueReplicas to getActiveReplicas. Lowering log printouts here and there


===============
Version v6r6p12
===============

DMS
===

Bugfix
:::::::::::

 - RemovalTask - Replacing "'" by "" in error str set as attribute for a subRequest file. Without that request cannot be updated when some nasty error occurs.


===============
Version v6r6p11
===============

RMS:
====

Bugfix
:::::::::::

 - RequestClient - log string formatting

DMS
===

Bugfix
:::::::::::

 - RemovalTask - handling for files not existing in the catalogue

Transformation
==============

Bugfix
:::::::::::

 - TransformationManager - ignore files in NotProcessed status to get the % of processed files

Interfaces
==========

Bugfix
:::::::::::

 - Fixes due to the recent changes in PromptUser utility


===============
Version v6r6p10
===============

RMS
===

Bugfix
:::::::::::

 - RequestDBMySQL - better escaping of queries

WMS
===

Bugfix
:::::::::::

 - SiteDirector - get compatible platforms before checking Task Queues for a site


==============
Version v6r6p9
==============

Core
====

Bugfix
:::::::::::

 - Utilities/PromptUser.py - better user prompt

Accounting
==========

Feature
::::::::::::

 - Add some validation to the job records because of weird data coming from YANDEX.ru

DMS
===

Bugfix
:::::::::::

 - ReplicaManager - typo errStr -> infoStr in __replicate()
 - FTSRequest - fixed log message

WMS
===

Bugfix
:::::::::::

 - SiteDirector - use CSGlobals.getVO() call instead of explicit CS option


==============
Version v6r6p8
==============

Transformation
==============

Bugfix
:::::::::::

 - TransformationDB - typo in getTransformationFiles(): iterValues -> itervalues


==============
Version v6r6p7
==============

Resources
=========

Bugfix
:::::::::::

 - StorageFactory - uncommented line that was preventing the status to be returned
 - CE remote scripts - should return status and not call exit()
 - SSHComputingElement - wrong pilot ID reference


==============
Version v6r6p6
==============

WMS
===

Bugfix
:::::::::::

 - TaskQueueDB - in findOrphanJobs() retrieve orphaned jobs as list of ints instead of list of tuples
 - OptimizerExecutor - added import of datetime to cope with the old style optimizer parameters

Transformation
==============

Bugfix
:::::::::::

 - TransformationAgent - fix finalization entering in an infinite loop
 - TransformationCleaningAgent - treating the archiving delay
 - TransformationDB - fix in getTransformationFiles() in case of empty file list

Feature
::::::::::::

 - TransformationCLI - added resetProcessedFile command


==============
Version v6r6p5
==============

Transformation
==============

Bugfix
:::::::::::

 - TransformationAgent - type( transClient -> transfClient )
 - TransformationAgent - self._logInfo -> self.log.info
 - TransformationAgent - skip if no Unused files
 - TransformationAgent - Use CS option for replica cache lifetime

Change
:::::::::::

 - TransformationAgent - accept No new Unused files every [6] hours


==============
Version v6r6p4
==============

DMS
===

Bugfix
:::::::::::

 - TransferAgent - protection for files that can not be scheduled
 - TransferDB - typo (instIDList - > idList ) fixed

Transformation
==============

Bugfix
:::::::::::

 - TransformationAgent - typo ( loginfo -> logInfo )


==============
Version v6r6p3
==============

FIX: merged in patch v6r5p14


Core
====

Bugfix
:::::::::::

 - X509Chain - return the right structure in getCredentials() in case of failure
 - dirac-deploy-scripts.py - allow short scripts starting from "d"
 - dirac-deploy-scripts.py - added DCOMMANDS_PPID env variable in the script wrapper
 - ExecutorReactor - reduced error message dropping redundant Task ID

Interfaces
==========

Bugfix
:::::::::::

 - Dirac.py - allow to pass LFN list to replicateFile()

DMS
===

Bugfix
:::::::::::

 - FileManager - extra check if all files are available in _findFiles()
 - FileCatalogClientCLI - bug in DirectoryListing


==============
Version v6r6p2
==============

FIX: merged in patch v6r5p13


WMS
===

Bugfix
:::::::::::

 - SiteDirector - if no community set, look for DIRAC/VirtualOrganization setting

Framework
=========

Bugfix
:::::::::::

 - SystemLoggingDB - LogLevel made VARCHAR in the MessageRepository table
 - Logging - several log messages are split in fixed and variable parts
 - SystemLoggingDB - in insertMessage() do not insert new records in auxiliary tables if they are already there


==============
Version v6r6p1
==============

Core:
=====

Change
:::::::::::

 - PromptUser - changed log level of the printout to NOTICE

Feature
::::::::::::

 - Base Client constructor arguments are passed to the RPCClient constructor

DMS:
====

Feature
::::::::::::

 - FTSRequest - added a prestage mechanism for source files
 - FileCatalogClientCLI - added -f switch to the size command to use raw faile tables instead of storage usage tables
 - FileCatalog - added orphan directory repair tool
 - FIleCatalog - more counters to control the catalog sanity

WMS:
====

Bugfix
:::::::::::

 - SandboxStoreClient - no more kwargs tricks
 - SandboxStoreClient returns sandbox file name in case of upload failure to allow failover
 - dirac-pilot - fixed VO_%s_SW_DIR env variable in case of OSG

TS:
===

Bugfix
:::::::::::

 - TransformationManagerHandler - avoid multiple Operations() instantiation in getTransformationSummaryWeb()


============
Version v6r6
============

Core
====

Bugfix
:::::::::::

 - dirac-install - properly parse += in .cfg files
 - Graphs.Utilities - allow two lines input in makeDataFromCVS()
 - Graphs - allow Graphs package usage if even matplotlib is not installed

Change
:::::::::::

 - getDNForUsername helper migrated from Core.Security.CS to Registry helper
 - The DIRAC.Core.Security.CS is replaced by the Registry helper
 - MessageClient(Factor) - added msgClient attribute to messages

Feature
::::::::::::

 - SiteSEMapping - new utilities getSitesGroupedByTierLevel(), getTier1WithAttachedTier2(), getTier1WithTier2
 - dirac-compile-externals will retrieve the Externals compilation scripts from it's new location in github (DIRACGrid/Externals)
 - Possibility to define a thread-global credentials for DISET connections (for web framework)
 - Logger - color output ( configurable )
 - dirac-admin-sort-cs-sites - to sort sites in the CS
 - Core.Security.Properties - added JOB_MONITOR and USER_MANAGER properties

Configuration
=============

Feature
::::::::::::

 - Registry - added getAllGroups() method

Framework
=========

Feature
::::::::::::

 - SystemAdministratorClientCLI - possibility to define roothPath and lcgVersion when updating software

Accounting
==========

Bugfix
:::::::::::

 - DBUtils - plots going to greater granularity

Feature
::::::::::::

 - JobPlotter - added Normalized CPU plots to Job accounting

DMS
===

Bugfix
:::::::::::

 - FileCatalog - addMetadataField() allow generic types, e.g. string
 - FileCatalog - path argument is normalized before usage in multiple methods
 - FileCatalog - new metadata for files(directories) should not be there before for directories(files)
 - FileCatalogClientCLI - in do_ls() check properly the path existence
 - FileCatalogClientCLI - protection against non-existing getCatalogCounters method in the LFC client
 - DMS Agents - properly call superclass constructor with loadName argument
 - ReplicaManager - in removeFile() non-existent file is marked as failed
 - Make several classes pylint compliant: DataIntegrityHandler, DataLoggingHandler, FileCatalogHandler, StorageElementHandler, StorageElementProxyHandler, TransferDBMonitoringHandler
 - LogUploadAgent - remove the OSError exception in __replicate()
 - FileCatalogClientCLI - multiple check of proper command inputs, automatic completion of several commands with subcommands, automatic completion of file names
 - dirac-admin-ban-se - allow to go over all options read/write/check for each SE
 - ReplicaManager - removed usage of obsolete "/Resources/StorageElements/BannedTarget"

Change
:::::::::::

 - FileCatalog - forbid removing non-empty directories
 - FileCatalogClientCLI - reformat the output of size command
 - removed StorageUsageClient.py
 - removed obsoleted ProcessingDBAgent.py

Feature
::::::::::::

 - FileCatalog - storage usage info stored in all the directories, not only those with files
 - FileCatalog - added utility to rebuild storage usage info from scratch
 - FileCatalog - added method for rebuilding DirectoryUsage data from scratch
 - FileCatalog - Use DirectoryUsage mechanism for both logical and physical storage
 - StrategyHandler - new implementation to speed up file scheduling + better error reporting
 - LcgFileCatalogProxy - moved from from LHCbDirac to DIRAC

WMS
===

Bugfix
:::::::::::

 - SiteDirector - provide list of sites to the Matcher in the initial query
 - SiteDirector - present a list of all groups of a community to match TQs
 - Matcher - proper reporting pilot site and CE
 - PilotStatusAgent - use getPilotProxyFromDIRACGroup() instead of getPilotProxyFromVOMSGroup()
 - WMSAdministrator, SiteDirector - store only non-empty pilot output to the PilotDB
 - JobManager - reconnect to the OptimizationMind in background if not yet connected

Change
:::::::::::

 - RunNumber job parameter was removed from all the relevant places ( JDL, JobDB, etc )
 - Get rid of LHCbPlatform everywhere except TaskQueueDB
 - dirac-boinc-pilot dropped
 - TaskQueueDirector does not depend on /LocalSite section any more
 - reduced default delays for JobCleaningAgent
 - limit the number of jobs received by JobCleaningAgent
 - JobDB - use insertFields instead of _insert
 - Matcher, TaskQueueDB - switch to use Platform rather than LHCbPlatform retaining LHCbPlatform compatibility
 - JobManager - improved job Killing/Deleting logic
 - dirac-pilot - treat the OSG case when jobs on the same WN all run in the same directory
 - JobMonitoringHandler - add cutDate and condDict parameters to getJobGroup()
 - JobManifest - use Operations helper

Feature
::::::::::::

 - dirac-pilot - add environment setting for SSH and BOINC CEs
 - WMSAdministrator - get output for non-grid CEs if not yet in the DB
 - JobAgent - job publishes BOINC parameters if any
 - JobWrapper - added more status reports on different failures
 - JobMonitoringHandler - check access rights with JobPolicy when accessing job info from the web
 - JobManager,JobWrapper - report to accounting jobs in Rescheduled final state if rescheduling is successful
 - added killPilot() to the WMSAdministrator interface, DiracAdmin and dirac-admin-kill-pilot command
 - TimeLeft - renormalize time left using DIRAC Normalization if available
 - JobCleaningAgent - delete logging records from JobLoggingDB when deleting jobs

RMS
===

Bugfix
:::::::::::

 - RequestDBFile - better exception handling in case no JobID supplied
 - RequestManagerHandler - make it pylint compliant

Change
:::::::::::

 - Major revision of the code
 - RequestDB - added index on SubRequestID in the Files table
 - RequestClient - readRequestForJobs updated to the new RequetsClient structure

Feature
::::::::::::

 - RequestProxyHandler - is forwarding requests from voboxes to central RequestManager. If central RequestManager is down, requests are dumped into file cache and a separate thread running in background is trying to push them into the central.

RSS
===

Feature
::::::::::::

 - CS.py - Space Tokens were hardcoded, now are obtained after scanning the StorageElements.

Resources
=========

Bugfix
:::::::::::

 - SSHComputingElement - enabled multiple hosts in one queue, more debugging

Change
:::::::::::

 - SSHXXX Computing Elements - define SSH class once in the SSHComputingElement
 - Get rid of legacy methods in ComputingElement
 - put common functionality into SSHComputingElement base class for all SSHxxx CEs

Feature
::::::::::::

 - SSHComputingElement - added option to define private key location
 - enable definition of ChecksumType per SE
 - SSHBatch, SSHCondor Computing Elements
 - SSHxxx Computing Elements - using remote control scripts to better capture remote command errors
 - added killJob() method tp all the CEs
 - FileCatalog - take the catalog information info from /Operations CS section, if defined there, to allow specifications per VO

Interfaces
==========

Bugfix
:::::::::::

 - Dirac.py - when running in mode="local" any directory in the ISB would not get untarred, contrary to what is done in the JobWrapper

Change
:::::::::::

 - Removed Script.initialize() from the API initialization
 - Some general API polishing

TS
==

Bugfix
:::::::::::

 - TaskManager - bug fixed in treating tasks with input data
 - TransformationCleaningAgent - properly call superclass constructor with loadName argument
 - TransformationDB - wrong SQL statement generation in setFileStatusForTransformation()

Change
:::::::::::

 - TransformationCleaningAgent - removed usage of StorageUsageClient

Feature
::::::::::::

 - TransformationCleaningAgent - added _addExtraDirectories() method to extend the list of directories to clean in a subclass if needed
 - TransformationAgent is multithreaded now ( implementation moved from LHCbDIRAC )
 - added unit tests
 - InputDataAgent - possibility to refresh only data registered in the last predefined period of time
 - TransformationAgent(Client) - management of derived transformations and more ported from LHCbDIRAC


===============
Version v6r5p14
===============

Core
====

Feature
::::::::::::

 - Utilities - added Backports utility

WMS
===

Bugfix
:::::::::::

 - Use /Operations/JobScheduling section consistently, drop /Operations/Matching section
 - Executors - several fixes

Feature
::::::::::::

 - Allow VO specific share correction plugins from extensions


===============
Version v6r5p13
===============

WMS
===

Bugfix
:::::::::::

 - Executors - VOPlugin will properly send and receive the params
 - Correctors - Properly retrieve info from the CS using the ops helper

Feature
::::::::::::

 - Correctors can be defined in an extension


===============
Version v6r5p12
===============

FIX: merged in patch v6r4p34



===============
Version v6r5p11
===============

FIX: merged in patch v6r4p33


Core
====

Bugfix
:::::::::::

 - MySQL - added offset argument to buildConditions()


===============
Version v6r5p10
===============

FIX: merged in patch v6r4p32



==============
Version v6r5p9
==============

FIX: merged in patch v6r4p30



==============
Version v6r5p8
==============

FIX: merged in patch v6r4p29



==============
Version v6r5p7
==============

FIX: merged in patch v6r4p28



==============
Version v6r5p6
==============

FIX: merged in patch v6r4p27


Transformation
==============

Bugfix
:::::::::::

 - TransformationDB - StringType must be imported before it can be used

RSS
===

Feature
::::::::::::

 - CS.py - Space Tokens were hardcoded, now are obtained after scanning the StorageElements.


==============
Version v6r5p5
==============

FIX: merged in patch v6r4p26



==============
Version v6r5p4
==============

FIX: merged in patch v6r4p25



==============
Version v6r5p3
==============

Transformation
==============

Bugfix
:::::::::::

 - merged in patch v6r4p24


==============
Version v6r5p2
==============

Web
===

Feature
::::::::::::

 - includes DIRACWeb tag web2012092101


==============
Version v6r5p1
==============

Core
====

Bugfix
:::::::::::

 - ExecutorMindHandler - return S_OK() in the initializeHandler
 - OptimizationMindHandler - if the manifest is not dirty it will not be updated by the Mind

Configuration
=============

Feature
::::::::::::

 - Resources helper - added getCompatiblePlatform(), getDIRACPlatform() methods

Resources
=========

Bugfix
:::::::::::

 - SSHComputingElement - add -q option to ssh command to avoid banners in the output
 - BOINCComputingElement - removed debugging printout
 - ComputingElement - use Platform CS option which will be converted to LHCbPlatform for legacy compatibility

DMS
===

Bugfix
:::::::::::

 - RequestAgentBase - lowering loglevel from ALWAYS to INFO to avoid flooding SystemLogging

WMS:
====

Bugfix
:::::::::::

 - SiteDirector - provide CE platform parameter when interrogating the TQ
 - GridPilotDirector - publish pilot OwnerGroup rather than VOMS role
 - WMSUtilities - add new error string into the parsing of the job output retrieval


============
Version v6r5
============

NEW: Executor framework


Core
====

Bugfix
:::::::::::

 - ProcessPool - killing stuck workers after timeout
 - dirac-install - add -T/--Timeout option to define timeout for distribution downloads
 - avoid PathFinder.getServiceURL and use Client class ( DataLoggingClient,LfcFileCatalogProxyClient )
 - MySQL - added TIMESTAMPADD and TIMESTAMPDIFF to special values not to be scaped by MySQL
 - Convert to string before trying to escape value in MySQL
 - X509Chain - avoid a return of error when the group is not valid
 - MySQL - reduce verbosity of log messages when high level methods are used
 - Service.py - check all return values from all initializers

Change
:::::::::::

 - DB will throw a RuntimeException instead of a sys.exit in case it can't contact the DB
 - Several improvements on DISET
 - Fixed all DOS endings to UNIX
 - Agents, Services and Executors know how to react to CSSection/Module and react accordingly
 - dirac-distribution - added global defaults flag and changed the flag to -M or --defaultsURL
 - Component installation procedure updated to cope with components inheriting Modules
 - InstallTools - use dirac- command in runit run scripts
 - Several DB classes have been updated to use the MySQL buildCondition method

Feature
::::::::::::

 - MySQL.py - added Test case for Time.dateTime time stamps
 - MySQL.py - insertFields and updateFields can get values via Lists or Dicts
 - DataIntegrityDB - use the new methods from MySQL and add test cases
 - DataIntegrityHandler - check connection to DB and create tables (or update their schema)
 - DataLoggingDB - use the new methods from MySQL and add test cases
 - DataLoggingHandler - check connection to DB and create tables (or update their schema)
 - install tools are updated to deal with executors
 - dirac-install - added possibility of defining dirac-install's global defaults by command line switch
 - ObjectLoader utility
 - DISET Services - added PacketTimeout option
 - SystemLoggingDB - updated to use the renewed MySQL interface and SQL schema
 - Added support for multiple entries in /Registry/DefaultGroup, for multi-VO installations
 - MySQL - provide support for greater and smaller arguments to all MySQL high level methods

Configuration
=============

Change
:::::::::::

 - By default return option and section lists ordered as in the CS

Feature
::::::::::::

 - ConfigurationClient - added function to refresh remote configuration

Framework
=========

Bugfix
:::::::::::

 - Registry.findDefaultGroup will never return False

Change
:::::::::::

 - ProxyManager does not accept proxies without explicit group
 - SystemAdministratorHandler - force refreshing the configuration after new component setup

RSS
===

Change
:::::::::::

 - removed code execution from __init__
 - removed unused methods

Feature
::::::::::::

 - Log all policy results

Resources
=========

Bugfix
:::::::::::

 - SGETimeLeft - better parsing of the batch system commands output
 - InProcessComputingElement - when starting a new job discard renewal of the previous proxy

Feature
::::::::::::

 - updated SSHComputingElement which allows multiple job submission
 - BOINCComputingElement - new CE client to work with the BOINC desktop grid infrastructure

WMS
===

Bugfix
:::::::::::

 - typo in JobLoggingDB
 - DownloadInputData - when not enough disk space, message was using "buffer" while it should be using "data"
 - the sandboxmetadataDB explosion when using the sandboxclient without direct access to the DB
 - InputDataResolution - just quick mod for easier extensibility, plus removed some LHCb specific stuff
 - StalledJobAgent - use cpuNormalization as float, not string
 - Don't kill an executor if a task has been taken out from it
 - SiteDirector - better handling of tokens and filling mode
 - StalledJobAgent - default startTime and endTime to "now", avoid None value

Change
:::::::::::

 - WMS Optimizers are now executors
 - SandboxStoreClient can directly access the DB if available
 - Moved JobDescription and improved into JobManifest
 - Whenever a DB is not properly initialized it will raise a catchable RuntimeError exception instead of silently returning
 - Natcher - refactor to simpify the logic, introduced Limiter class
 - Treat MaxCPUTime and CPUTime the same way in the JDL to avoid confusion
 - JobAgent - provide resource description as a dictionary to avoid extra JDL parsing by the Matcher
 - Matcher - report pilot info once instead of sending it several times from the job
 - Matcher - set the job site instead of making a separate call to JobStateUpdate
 - Disabled TQs can also be matched, if no jobs are there, a retry will be triggered

Feature
::::::::::::

 - JobState/CachedJobState allow access to the Job via DB/JobStateSync Service automatically
 - Added support for reset/reschedule in the OptimizationMind
 - allow jobids in a file in dirac-wms-job-get-output
 - JobManager - zfill in %n parameter substitution to allow alphabetical sorting
 - Directors - added checking of the TaskQueue limits when getting eligible queues
 - SiteDirector - added options PilotScript, MaxPilotsToSubmit, MaxJobsInFillMode
 - dirac-boinc-pilot - pilot script to be used on the BOINC volunteer nodes
 - Generic pilot identities are automatically selected by the TQD and the SiteDirector if not explicitly defined in /Pilot/GenericDN and GenericGroup
 - Generic pilot groups can have a VO that will be taken into account when selecting generic credentials to submit pilots
 - Generic pilots that belong to a VO can only match jobs from that VO
 - StalledJobAgent - added rescheduling of jobs stuck in Matched or Rescheduled status
 - JobAgent - stop after N failed matching attempts (nothing to do), use StopAfterFailedMatches option
 - Matcher - added Matches done and matches OK statistics
 - TaskQueue - don't delete fresh task queues. Wait 5 minutes to do so.

Transformation
==============

Bugfix
:::::::::::

 - TransformationAgent - a small improvement: now can pick the prods status to handle from the CS, plus few minor corrections (e.g. logger messages)
 - TransformationCLI - take into accout possible failures in resetFile command

Accounting
==========

Bugfix
:::::::::::

 - AccountingDB - fixed some logic for readonly cases
 - Calculate the rebucket ETA using remaining records to be processed instead of the total records to be processed
 - Plots with no data still carry the plot name

Change
:::::::::::

 - Added new simpler and faster bucket insertion mechanism

Feature
::::::::::::

 - AccountingDB - added retrieving RAW records for internal stuff
 - Added more info when rebucketing

DMS
===

Bugfix
:::::::::::

 - DataLoggingClient and DataLoggingDB - tests moved to separate files

Change
:::::::::::

 - request agents cleanup

Feature
::::::::::::

 - SRM2Storage - added retry in the gfal calls
 - added new FTSCleaningAgent cleaning up TransferDB tables

RMS
===

Change
:::::::::::

 - Stop using RequestAgentMixIn in the request agents


===============
Version v6r4p34
===============

DMS
===

Bugfix
:::::::::::

 - FileCatalogCLI - fixed wrong indentation

Change
:::::::::::

 - RegistrationTask - removed some LHCb specific defaults


===============
Version v6r4p33
===============

DMS
===

Change
:::::::::::

 - FTSRequest - be more verbose if something is wrong with file


===============
Version v6r4p32
===============

WMS
===

Bugfix
:::::::::::

 - StalledJobAgent - avoid exceptions in the stalled job accounting reporting

DMS
===

Feature
::::::::::::

 - FTSMonitorAgent - handling of expired FTS jobs

Interfaces
==========

Change
:::::::::::

 - Dirac.py - attempt to retrieve output sandbox also for Completed jobs in retrieveRepositorySandboxes()


===============
Version v6r4p30
===============

Core
====

Bugfix
:::::::::::

 - dirac-admin-bdii-ce-voview - proper check of the result structure

Interfaces
==========

Bugfix
:::::::::::

 - Dirac.py, Job.py - allow to pass environment variables with special characters

DMS
===

Feature
::::::::::::

 - FileCatalogCLI - possibility to sort output in the ls command

WMS:
====

Bugfix
:::::::::::

 - JobWrapper - interpret environment variables with special characters


===============
Version v6r4p29
===============

RMS
===

Bugfix
:::::::::::

 - RequestDBMySQL - wrong indentation in __updateSubRequestFiles()


===============
Version v6r4p28
===============

Interfaces
==========

Change
:::::::::::

 - Dirac.py, DiracAdmin.py - remove explicit timeout on RPC client instantiation

RSS
===

Bugfix
:::::::::::

 - CS.py - fix for updated CS location (backward compatible)

DMS
===

Bugfix
:::::::::::

 - StrategyHandler - bug fixed determineReplicationTree()
 - FTSRequest - add checksum string to SURLs file before submitting an FTS job

WMS
===

Bugfix
:::::::::::

 - JobWrapper - protection for double quotes in JobName

Change
:::::::::::

 - SiteDirector - switched some logging messages from verbose to info level

RMS
===

Feature
::::::::::::

 - Request(Client,DBMySQL,Manager) - added readRequestsForJobs() method


===============
Version v6r4p27
===============

DMS
===

Bugfix
:::::::::::

 - SRM2Storage - removed hack for EOS (fixed server-side)

Transformation
==============

Change
:::::::::::

 - TransformationClient - limit to 100 the number of transformations in getTransformations()

Feature
::::::::::::

 - TransformationAgent - define the transformations type to use in the configuration

Interfaces
==========

Bugfix
:::::::::::

 - Job.py -  fix for empty environmentDict (setExecutionEnv)


===============
Version v6r4p26
===============

Transformation
==============

Bugfix
:::::::::::

 - TransformationClient - fixed calling sequence in rpcClient.getTransformationTasks()

Feature
::::::::::::

 - TransformationClient - added log messages in verbose level.


===============
Version v6r4p25
===============

DMS
===

Bugfix
:::::::::::

 - StrategyHandler - sanity check for wrong replication tree


===============
Version v6r4p24
===============

Core
====

Feature
::::::::::::

 - MySQL - add 'offset' argument to the buildCondition()

Transformation
==============

Bugfix
:::::::::::

 - TransformationAgent - randomize the LFNs for removal/replication case when large number of those
 - TransformationAgent(DB) - do not return redundant LFNs in getTransformationFiles()

Change
:::::::::::

 - TransformationClient(DB,Manager) - get transformation files in smaller chunks to improve performance


===============
Version v6r4p23
===============

Web
===

Feature
::::::::::::

 - includes DIRACWeb tag web2012092101


===============
Version v6r4p22
===============

DMS
===

Bugfix
:::::::::::

 - SRM2Storage - fix the problem with the CERN-EOS storage


===============
Version v6r4p21
===============

Core
====

Bugfix
:::::::::::

 - SGETimeLeft - take into account dd:hh:mm:ss format of the cpu consumed


===============
Version v6r4p20
===============

WMS
===

Bugfix
:::::::::::

 - PilotDirector, GridPilotDirector - make sure that at least 1 pilot is to be submitted
 - GridPilotDirector - bug on how pilots are counted when there is an error in the submit loop.
 - dirac-pilot - proper install script installation on OSG sites


===============
Version v6r4p19
===============

RMS
===

Bugfix
:::::::::::

 - RequestDBMySQL - optimized request selection query


===============
Version v6r4p18
===============

Configuration
=============

Bugfix
:::::::::::

 - CE2CSAgent.py - the default value must be set outside the loop

DMS
===

Bugfix
:::::::::::

 - dirac-dms-fts-submit, dirac-dms-fts-monitor - print out error messages

Feature
::::::::::::

 - dirac-dms-create-replication-request

Resources
=========

Bugfix
:::::::::::

 - TorqueComputingElement.py, plus add UserName for shared Queues

WMS
===

Bugfix
:::::::::::

 - JobManagerHandler - default value for pStart (to avoid Exception)


===============
Version v6r4p17
===============

Core
====

Bugfix
:::::::::::

 - dirac-configure - setup was not updated in dirac.cfg even with -F option
 - RequestHandler - added fix for Missing ConnectionError

DMS
===

Bugfix
:::::::::::

 - dirac-dms-clean-directory - command fails with `KeyError: 'Replicas'`.

WMS
===

Bugfix
:::::::::::

 - SiteDirector - adapt to the new method in the Matcher getMatchingTaskQueue
 - SiteDirector - added all SubmitPools to TQ requests


===============
Version v6r4p16
===============

Core:
=====

Bugfix
:::::::::::

 - dirac-install - bashrc/cshrc were wrongly created when using versionsDir

Accounting
==========

Change
:::::::::::

 - Added new simpler and faster bucket insertion mechanism

Feature
::::::::::::

 - Added more info when rebucketing

WMS
===

Bugfix
:::::::::::

 - Matcher - bad codition if invalid result

Change
:::::::::::

 - Matcher - refactored to take into account job limits when providing info to directors

Feature
::::::::::::

 - JoAgent - reports SubmitPool parameter if applicable


===============
Version v6r4p15
===============

WMS
===

Bugfix
:::::::::::

 - gLitePilotDirector - fix the name of the MyProxy server to avoid crasehs of the gLite WMS

Transformation
==============

Bugfix
:::::::::::

 - TaskManager - when the file is on many SEs, wrong results were generated


===============
Version v6r4p13
===============

DMS
===

Bugfix
:::::::::::

 - dirac-admin-allow-se - added missing interpreter line


===============
Version v6r4p12
===============

DMS
===

Change
:::::::::::

 - RemovalTask - for DataManager shifter change creds after failure of removal with her/his proxy.

RSS
===

Bugfix
:::::::::::

 - ResourceManagementClient  - Fixed wrong method name

Feature
::::::::::::

 - Added RssConfiguration class


===============
Version v6r4p11
===============

Core
====

Bugfix
:::::::::::

 - GGUSTicketsClient - GGUS SOAP URL updated

DMS
===

Bugfix
:::::::::::

 - ReplicaManager - wrong for loop

RequestManagement
=================

Bugfix
:::::::::::

 - RequestClient - bug fix in finalizeRequest()

Transformation
==============

Bugfix
:::::::::::

 - TaskManager - fix for correctly setting the sites (as list)


===============
Version v6r4p10
===============

RequestManagement
=================

Bugfix
:::::::::::

 - RequestContainer - in addSubrequest() function

Resources
=========

Bugfix
:::::::::::

 - SRM2Storage - in checksum type evaluation

ResourceStatusSystem
====================

Bugfix
:::::::::::

 - InfoGetter - wrong import statement

WMS
===

Bugfix
:::::::::::

 - SandboxMetadataDB - __init__() can not return a value


==============
Version v6r4p9
==============

DMS
===

Change
:::::::::::

 - FailoverTransfer - ensure the correct execution order of the subrequests


==============
Version v6r4p8
==============

Bring in fixes from v6r3p17


Core:
=====

Bugfix
:::::::::::

 - Don't have the __init__ return True for all DBs
 - Operations will now look in 'Defaults' instead of 'Default'

Feature
::::::::::::

 - Added more protection for exceptions thrown in callbacks for the ProcessPool

DataManagement:
===============

Bugfix
:::::::::::

 - Put more protection in StrategyHandler for neither channels  not throughput read out of TransferDB
 - No JobIDs supplied in getRequestForJobs function for RequestDBMySQL taken into account
 - Fix on getRequestStatus

Change
:::::::::::

 - RequestClient proper use of getRequestStatus in finalizeRequest
 - Refactored RequestDBFile


==============
Version v6r4p7
==============

WorkloadManagement
==================

Bugfix
:::::::::::

 - SandboxMetadataDB won't explode DIRAC when there's no access to the DB

Change
:::::::::::

 - Whenever a DB fails to initialize it raises a catchable exception instead of just returning silently

DataManagement
==============

Change
:::::::::::

 - Added Lost and Unavailable to the file metadata


==============
Version v6r4p6
==============

Bring fixes from v6r4p6



==============
Version v6r4p5
==============

Configuration
=============

Feature
::::::::::::

 - Added function to generate Operations CS paths

Core
====

Bugfix
:::::::::::

 - Added proper ProcessPool checks and finalisation

DataManagement
==============

Bugfix
:::::::::::

 - don't set Files.Status to Failed for non-existign files, failover transfers won't go
 - remove classmethods here and there to unblock requestHolder
 - sorting replication tree by Ancestor, not hopAncestorgit add DataManagementSystem/Agent/TransferAgent.py
 - if there is no failed files, put an empty dict

Change
:::::::::::

 - RAB, TA: change task timeout: 180 and 600 (was 600 and 900 respectively)
 - TransferAgent: add AcceptableFailedFiles to StrategyHandler to ban FTS channel from scheduling

Feature
::::::::::::

 - TA: add finalize

RSS
===

Bugfix
:::::::::::

 - RSS is setting Allowed but the StorageElement checks for Active

Workflows
=========

Bugfix
:::::::::::

 - Part of WorfklowTask rewritten to fix some issues and allow 'ANY' as site

Transformation
==============

Bugfix
:::::::::::

 - Wrong calls to TCA::cleanMetadataCatalogFiles


==============
Version v6r4p4
==============

Core
====

Bugfix
:::::::::::

 - Platform.py - check if Popen.terminate is available (only from 2.6)


==============
Version v6r4p3
==============

Core
====

Bugfix
:::::::::::

 - ProcessPool with watchdog and timeouts - applied in v6r3 first


==============
Version v6r4p2
==============

StorageManagement
=================

Bugfix
:::::::::::

 - StorageElement - staging is a Read operation and should be allowed as such

WMS
===

Bugfix
:::::::::::

 - InProcessComputingElement, JobAgent - proper return status code from the job wrapper

Core
====

Bugfix
:::::::::::

 - Platform - manage properly the case of exception in the ldconfig execution


==============
Version v6r4p1
==============

DMS
===

Bugfix
:::::::::::

 - TransferDB.getChannelObservedThroughput - the channelDict was created in a wrong way

RSS
===

Bugfix
:::::::::::

 - ResourceStatus was not returning Allowed by default


============
Version v6r4
============

Core
====

Bugfix
:::::::::::

 - dirac-install-db.py: addDatabaseOptionsToCS has added a new keyed argument
 - If several extensions are installed, merge ConfigTemplate.cfg
 - ProcessPool - fixes in the locking mechanism with LockRing, stopping workers when the parent process is finished
 - Added more locks to the LockRing

Feature
::::::::::::

 - SGETimeLeft.py: Support for SGE backend
 - Service framework - added monitoring of file descriptors open
 - Service framework - Reduced handshake timeout to prevent stuck threads
 - MySQL class with new high level methods - buildCondition,insertFields,updateFields deleteEntries, getFields, getCounters, getDistinctAttributeValues
 - The installation tools are updated to install components by name with the components module specified as an option

DMS
===

Bugfix
:::::::::::

 - TransferDB.py - speed up the Throughput determination
 - FileCatalogCLI - replicate operation does a proper replica registration ( closes #5 )
 - ReplicaManager - __cleanDirectory now working and thus dirac-dms-clean-directory

Feature
::::::::::::

 - dirac-dms-add-files: script similar to dirac-dms-remove-files, allows for 1 file specification on the command line, using the usual dirac-dms-add-file options, but also can take a text file in input to upload a bunch of files. Exit code is 0 only if all was fine and is different for every error found.
 - StorageElementProxy- support for data downloading with http protocol from arbitrary storage, needed for the web data download

WMS
===

Bugfix
:::::::::::

 - StalledJobAgent - StalledTimeHours and FailedTimeHours are read each cycle, refer to the Watchdog heartBeat period (should be renamed); add NormCPUTime to Accounting record
 - StalledJobAgent - get ProcessingType from JDL if defined
 - dirac-wms-job-peek - missing printout in the command
 - properly report CPU usage when the Watchdog kill the payload.

Feature
::::::::::::

 - CPU normalization script to run a quick test in the pilot, used by the JobWrapper to report the CPU consumption to the accounting
 - SiteDirector - support for the operation per VO in multi-VO installations
 - SiteDirector - take into account the number of already waiting pilots when evaluating the number of pilots to submit

RSS
===

Bugfix
:::::::::::

 - Result in ClientCache table is a varchar, but the method was getting a datetime

Change
:::::::::::

 - RSS components get operational parameters from the Operations handler

Feature
::::::::::::

 - CacheFeederAgent - VOBOX and SpaceTokenOccupancy commands added (ported from LHCbDIRAC)

DataManagement
==============

Bugfix
:::::::::::

 - if there is no failed files, put an empty dict

Transformation
==============

Bugfix
:::::::::::

 - Wrong calls to TCA::cleanMetadataCatalogFiles


===============
Version v6r3p19
===============

WMS
===

Bugfix
:::::::::::

 - gLitePilotDirector - fix the name of the MyProxy server to avoid crashes of the gLite WMS


===============
Version v6r3p18
===============

Resources
=========

Bugfix
:::::::::::

 - SRM2Storage - in checksum type evaluation


===============
Version v6r3p17
===============

DataManagement
==============

Bugfix
:::::::::::

 - Fixes issues #783 and #781. Bugs in ReplicaManager removePhisicalReplica and getFilesFromDirectory
 - Return S_ERROR if missing jobid arguments

Feature
::::::::::::

 - Checksum can be verified during FTS and SRM2Storage


===============
Version v6r3p16
===============

DataManagement
==============

Bugfix
:::::::::::

 - better monitoring of FTS channels
 - Handle properly None value for channels and bandwidths

Core
====

Bugfix
:::::::::::

 - Properly calculate the release notes if there are newer releases in the release.notes file


===============
Version v6r3p15
===============

DataManagement
==============

Bugfix
:::::::::::

 - if there is no failed files, put an empty dict

Transformation
==============

Bugfix
:::::::::::

 - Wrong calls to TCA::cleanMetadataCatalogFiles


===============
Version v6r3p14
===============

Core
====

Bugfix
:::::::::::

 - ProcessPool.py: clean processing and finalisation
 - Pfn.py: don't check for 'FileName' in pfnDict

DMS
===

Bugfix
:::::::::::

 - TransferAgent.py,RemovalAgent.py,RegistrationAgent.py - unlinking of temp proxy files, corection of values sent to gMonitor
 - StrategyHandler - new config option 'AcceptableFailedFiles' to unblock scheduling for channels if problematic transfers occured for few files
 - ReplicaManager.py - reverse sort of LFNs when deleting files and directories to avoid blocks

Feature
::::::::::::

 - dirac-dms-show-fts-status.py: script showing last hour history for FTS channels
 - TransferDBMonitoringHandler.py: new function exporting FST channel queues
 - TransferAgent,RemovalAgent,RegistrationAgent - new confing options for setting timeouts for tasks and ProcessPool finalisation
 - moved StrategyHandler class def to separate file under DMS/private

TMS
===

Bugfix
:::::::::::

 - TransformationCleaningAgent.py: some refactoring, new way of disabling/enabline execution by 'EnableFlag' config option


===============
Version v6r3p13
===============

Core
====

Bugfix
:::::::::::

 - Added proper ProcessPool checks and finalisation

DataManagement
==============

Bugfix
:::::::::::

 - don't set Files.Status to Failed for non-existign files, failover transfers won't go
 - remove classmethods here and there to unblock requestHolder
 - sorting replication tree by Ancestor, not hopAncestorgit add DataManagementSystem/Agent/TransferAgent.py

Change
:::::::::::

 - RAB, TA: change task timeout: 180 and 600 (was 600 and 900 respectively)
 - TransferAgent: add AcceptableFailedFiles to StrategyHandler to ban FTS channel from scheduling

Feature
::::::::::::

 - TA: add finalize


===============
Version v6r3p12
===============

Core
====

Bugfix
:::::::::::

 - Platform.py - check if Popen.terminate is available (only from 2.6)


===============
Version v6r3p11
===============

Core
====

Bugfix
:::::::::::

 - ProcessPool with watchdog and timeouts


===============
Version v6r3p10
===============

StorageManagement
=================

Bugfix
:::::::::::

 - StorageElement - staging is a Read operation and should be allowed as such

WMS
===

Bugfix
:::::::::::

 - InProcessComputingElement, JobAgent - proper return status code from the job wrapper

Core
====

Bugfix
:::::::::::

 - Platform - manage properly the case of exception in the ldconfig execution


==============
Version v6r3p9
==============

DMS
===

Bugfix
:::::::::::

 - TransferDB.getChannelObservedThroughput - the channelDict was created in a wrong way


==============
Version v6r3p8
==============

Web
===

Change
:::::::::::

 - return back to the release web2012041601


==============
Version v6r3p7
==============

Transformation
==============

Bugfix
:::::::::::

 - TransformationCleaningAgent - protection from deleting requests with jobID 0


==============
Version v6r3p6
==============

Core
====

Bugfix
:::::::::::

 - dirac-install-db - proper key argument (follow change in InstallTools)
 - ProcessPool - release all locks every time WorkignProcess.run is executed, more fixes to come
 - dirac-configure - for Multi-Community installations, all vomsdir/vomses files are now created

WMS
===

Bugfix
:::::::::::

 - dirac-pilot - SGE batch ID was overwriting the CREAM ID
 - PilotDirector - protect the CS master if there are at least 3 slaves

Feature
::::::::::::

 - SiteDirector - add pilot option with CE name to allow matching of SAM jobs.
 - Watchdog - set LocalJobID in the SGE case


==============
Version v6r3p5
==============

Core:
=====

Bugfix
:::::::::::

 - ProcessPool - bug making TaskAgents hang after max cycles
 - Graphs - proper handling plots with data containing empty string labels
 - GateWay - transfers were using an old API
 - GateWay - properly calculate the gateway URL
 - Utilities/Pfn.py - bug in pfnunparse() when concatenating Path and FileName

Accounting
==========

Bugfix
:::::::::::

 - DataCache - set daemon the datacache thread
 - BasePlotter - proper handling of the Petabyte scale data

Feature
::::::::::::

 - ReportGenerator - make AccountingDB readonly

DMS:
====

Bugfix
:::::::::::

 - TransferAgent, RegistrationTask - typos


==============
Version v6r3p4
==============

DMS:
====

Bugfix
:::::::::::

 - TransferAgent - wrong value for failback in TA:execute


==============
Version v6r3p3
==============

Configuration
=============

Bugfix
:::::::::::

 - Operations helper - typo

DMS:
====

Bugfix
:::::::::::

 - TransferAgent - change the way of redirecting request to task


==============
Version v6r3p2
==============

DMS
===

Bugfix
:::::::::::

 - FTSRequest - updating metadata for accouting when finalizing FTS requests

Core
====

Bugfix
:::::::::::

 - DIRAC/__init__.py - default version is set to v6r3


==============
Version v6r3p1
==============

WMS
===

Change
:::::::::::

 - Use ResourcesStatus and Resources helpers in the InputDataAgent logic

Configuration
=============

Feature
::::::::::::

 - added getStorageElementOptions in Resources helper

DMS
===

Bugfix
:::::::::::

 - resourceStatus object created in TransferAgent instead of StrategyHandler


============
Version v6r3
============

Core
====

Feature
::::::::::::

 - Added protections due to the process pool usage in the locking logic

Resources
=========

Bugfix
:::::::::::

 - LcgFileCatalogClient - reduce the number of retries: LFC_CONRETRY = 5 to avoid combined catalog to be stuck on a faulty LFC server

RSS
===

Bugfix
:::::::::::

 - ResourceStatus - reworked helper to keep DB connections

DMS
===

Bugfix
:::::::::::

 - ReplicaManager::CatalogBase::_callFileCatalogFcnSingleFile() - wrong argument

RequestManagement
=================

Bugfix
:::::::::::

 - TaskAgents - set timeOut for task to 10 min (15 min)

Feature
::::::::::::

 - TaskAgents - fill in Error fields in case of failing operations

Interfaces
==========

Bugfix
:::::::::::

 - dirac-wms-select-jobs - wrong use of the Dirac API


==============
Version v6r2p9
==============

Core
====

Bugfix
:::::::::::

 - dirac-configure - make use of getSEsForSite() method to determine LocalSEs

WMS
===

Change
:::::::::::

 - Matcher - add Stalled to "Running" Jobs when JobLimits are applied
 - JobDB - allow to specify required platform as Platform JDL parameter, the specified platform is taken into account even without /Resources/Computing/OSCompatibility section

Feature
::::::::::::

 - DownloadInputData,InputDataByProtocol - check Files on Tape SEs are on Disk cache before Download or getturl calls from Wrapper

DMS
===

Bugfix
:::::::::::

 - TaskAgents - fix for non-existing files
 - change verbosity in failoverReplication
 - FileCatalog - remove properly metadata indices
 - FileManagerBase - bugfix in the descendants evaluation logic
 - TransferAgent and TransferTask - update Files.Status to Failed when ReplicaManager.replicateAndRegister will fail completely; when no replica is available at all.

Change
:::::::::::

 - dirac-admin-allow(ban)-se - removed lhcb-grid email account by default, and added switch to avoid sending email

Core
====

Bugfix
:::::::::::

 - dirac-pilot - default lcg bindings version set to 2012-02-20


==============
Version v6r2p8
==============

DMS:
====

Change
:::::::::::

 - TransferAgent - fallback to task execution if replication tree is not found


==============
Version v6r2p7
==============

WMS
===

Bugfix
:::::::::::

 - SiteDirector - wrong CS option use: BundleProxy -> HttpProxy
 - SiteDirector - use short lines in compressed/encoded files in the executable python script


==============
Version v6r2p6
==============

DataManagement
==============

Bugfix
:::::::::::

 - Bad logic in StrategyHandler:MinimiseTotalWait

Core
====

Change
:::::::::::

 - updated GGUS web portal URL

RSS
===

Bugfix
:::::::::::

 - meta key cannot be reused, it is popped from dictionary

Framework
=========

Bugfix
:::::::::::

 - The Gateway service does not have a handler
 - distribution notes allow for word wrap

Feature
::::::::::::

 - ConfingTemplate entry for Gateway

WorkloadManagement
==================

Bugfix
:::::::::::

 - avoid unnecessary call if no LFN is left in one of the SEs
 - When Uploading job outputs, try first Local SEs, if any


==============
Version v6r2p5
==============

RSS
===

Bugfix
:::::::::::

 - several minor bug fixes

RequestManagement
=================

Bugfix
:::::::::::

 - RequestDBMySQL - removed unnecessary request type check

DMS
===

Bugfix
:::::::::::

 - FileCatalogClienctCLI - wrong evaluation of the operation in the find command
 - ReplicaManager - wrong operation order causing failure of UploadLogFile module

Feature
::::::::::::

 - FileCatalog - added possibility to remove specified metadata for a given path

Core
====

Feature
::::::::::::

 - dirac-install - generate cshrc DIRAC environment setting file for the (t)csh

Interfaces
==========

Change
:::::::::::

 - Job - added InputData to each element in the ParametricInputData

WMS
===

Change
:::::::::::

 - dirac-jobexec - pass ParametericInputData to the workflow as a semicolon separated string


==============
Version v6r2p4
==============

WMS
===

Bugfix
:::::::::::

 - StalledJobAgent - protection against jobs with no PilotReference in their parameters
 - WMSAdministratorHandler - wrong argument type specification for getPilotInfo method

StorageManagement
=================

Bugfix
:::::::::::

 - RequestFinalizationAgent - no method existence check when calling RPC method


==============
Version v6r2p3
==============

WMS
===

Change
:::::::::::

 - Matcher - fixed the credentials check in requestJob() to simplify it

ConfigurationSystem
===================

Change
:::::::::::

 - Operations helper - fix that allow no VO to be defined for components that do not need it

Core
====

Bugfix
:::::::::::

 - InstallTools - when applying runsvctrl to a list of components make sure that the config server is treated first and the sysadmin service - last


==============
Version v6r2p2
==============

WMS
===

Bugfix
:::::::::::

 - Matcher - restored logic for checking private pilot asking for a given DN for belonging to the same group with JOB_SHARING property.


==============
Version v6r2p1
==============

RequestManagementSystem
=======================

Bugfix
:::::::::::

 - RequestCleaningAgent - missing import of the "second" interval definition


============
Version v6r2
============

General
=======

Bugfix
:::::::::::

 - replaced use of exec() python statement in favor of object method execution

Accounting
==========

Change
:::::::::::

 - Accounting 'byte' units are in powers of 1000 instead of powers of 1024 (closes #457)

Core
====

Bugfix
:::::::::::

 - DISET Clients are now thread-safe. Same clients used twice in different threads was not closing the previous connection
 - TransferClient closes connections properly
 - DISET Clients are now thread-safe. Same client used twice in different threads will not close the previous connection
 - dirac-install - execute dirac-fix-mysql-script, if available, to fix the mysql.server startup script
 - dirac-distribution - Changed obsoleted tar.list file URL
 - typo in dirac-admin-add-host in case of error

Change
:::::::::::

 - Pfn.py - pfnparse function rewritten for speed up and mem usage, unit test case added
 - Beautification and reduce wait times to improve performance
 - Add deprecated sections in the CS Operations helper to ease the transition
 - dirac-admin-allow(ban)-se - use diracAdmin.sendMail() instead of NotificationClient.sendMail()

Feature
::::::::::::

 - reduce wait times in DISET protocol machinery to improve performance
 - dirac-fix-mysql-script command to fix the mysql start-up script for the given installation
 - ProcessPool - added functionality to kill all children processes properly when destroying ProcessPool objects
 - CS Helper for LocalSite section, with gridEnv method
 - Grid module will use Local.gridEnv if nothing passed in the arguments

Framework
=========

Bugfix
:::::::::::

 - UserProfileDB - no more use of "type" variable as it is a reserved keyword

RequestManagement:
==================

Bugfix
:::::::::::

 - RequestDBFile - more consistent treatment of requestDB Path
 - RequestMySQL - Execution order is evaluated based on not Done state of subrequests

Feature
::::::::::::

 - RequestCleaningAgent - resetting Assigned requests to Waiting after a configurable period of time

RSS
===

Bugfix
:::::::::::

 - CacheFeederAgent - too verbose messages moved to debug instead of info level
 - fixed a bug preventing RSS clients to connect to the services
 - Proper services synchronization
 - Better handling of exceptions due to timeouts in GOCDBClient
 - RSS.Notification emails are sent again
 - Commands have been modified to return S_OK, S_ERROR inside the Result dict. This way, policies get a S_ERROR / S_OK object. CacheFeederAgent has been updated accordingly.
 - allow clients, if db connection fails, to reconnect ( or at least try ) to the servers.
 - MySQLMonkey - properly escaped all parameters of the SQL queries, other fixes.
 - Minor bugfixes spotted on the Web development
 - Removed useless decorator from RSS handlers
 - _checkFloat() checks INTEGERS, not datetimes

Change
:::::::::::

 - RSS Action now inherits from a base class, and Actions are more homogeneous, they all take a uniform set of arguments. The name of modules has been changed from PolType to Action as well.
 - access control using CS Authentication options. Default is SiteManager, and get methods are all.
 - ResourceStatus helper tool moved to RSS/Client directory, no RSS objects created if the system is InActive
 - Removed ClientFastDec decorator, using a more verbose alternative.
 - Removed useless usage of kwargs on helper functions.

Feature
::::::::::::

 - CleanerAgent renamed to CacheCleanerAgent
 - Updated RSS scripts, to set element statuses and / or tokens.
 - Added a new script, dirac-rss-synch
 - added getSESitesList method to RSSClient

DataManagement
==============

Bugfix
:::::::::::

 - dirac-dms-user-lfns - fixed the case when the baseDir is specified
 - FTS testing scripts were using sys.argv and getting confused if options are passed
 - DFC - avoid crash if no directories or files found in metadata query
 - FTSMonitor, FTSRequest - fixes in handling replica registration, setting registration requests in FileToCat table for later retry
 - Failover registration request in the FTS agents.
 - FTSMonitor - enabled to register new replicas if even the corresponding request were removed from the RequestManagement
 - StorageElement - check if SE has been properly initialized before executing any method
 - LFC client - protect against getting None in lfc.lfc_readdirxr( oDirectory, "" )
 - add extra protection in dump method of StorageElement base class

Change
:::::::::::

 - refactoring of DMS agents executing requests, allow requests from arbitrary users
 - DFC - optimization of the directory size evaluation
 - DFC - getCatalogCounters() update to show numbers of directories
 - LFC client getReplica() - make use of the new bulk method lfc.lfc_getreplicasl()
 - FailoverTransfer - create subrequest per catalog if more than one catalog

Feature
::::::::::::

 - DFC - allow to specify multiple replicas, owner, mode when adding files
 - Added CREATE TEMPORARY TABLES privilege to FileCatalogDB
 - lfc_dfc_copy script to migrate data from LFC to DFC
 - DFC - use DirectoryUsage tables for the storage usage evaluations
 - DFC - search by metadata can be limited to a given directory subtree
 - DFC - search by both directory and file indexed metadata
 - DFC FileCatalogHandler - define database location in the configuration
 - DFC - new FileCatalogFactory class, possibility to use named DFC services

Interface
=========

Bugfix
:::::::::::

 - Dirac.py - fix some type checking things
 - Dirac.py - the addFile() method can now register to more than 1 catalog.

Feature
::::::::::::

 - Job.py - added method to handle the parametric parameters in the workflow. They are made available to the workflow_commons via the key 'GenericParameters'.

WMS
===

Bugfix
:::::::::::

 - removed dependency of the JobSchedulingAgent on RSS. Move the getSiteTier functionality to a new CS Helper.
 - WMSAdministratorHandler - Replace StringType by StringTypes in the export methods argument type
 - JobAgent - Set explicitly UseServerCertificate to "no" for the job executable
 - SiteDirector passes jobExecDir to pilot, this defaults to "." for CREAM CEs. It can be set in the CS. It will not make use of $TMPDIR in this case.
 - Set proper project and release version to the SiteDirector
 - Added installation as an option to the pilots and random MyProxyServer

Feature
::::::::::::

 - dirac-pilot - change directory to $OSG_WN_TMP on OSG sites
 - Added "JobDelay" option for the matching, refactored and added CS options to the matcher
 - Support for parametric jobs with parameters that can be of List type

Resources
=========

Bugfix
:::::::::::

 - make sure lfc client will not try to connect for several days

Feature
::::::::::::

 - Added SSH Grid Engine Computing Element
 - Added SSH Computing Element

Transformation
==============

Bugfix
:::::::::::

 - TransformationDB - in setFileStatusForTransformation() reset ErrorCount to zero if "force" flag and    the new status is "unused"

Feature
::::::::::::

 - TransformationDB - added support for dictionary in metadata for the InputDataQuery mechanism


===============
Version v6r1p13
===============

WMS
===

Bugfix
:::::::::::

 - JobSchedulingAgent - backported from v6r2 use of Resources helper


===============
Version v6r1p12
===============

Accounting
==========

Bugfix
:::::::::::

 - Properly delete cached plots

Core
====

Bugfix
:::::::::::

 - dirac-install - run externals post install after generating the versions dir


===============
Version v6r1p11
===============

Core
====

Bugfix
:::::::::::

 - dirac-distribution - properly generate releasehistory and releasenotes

Feature
::::::::::::

 - dirac-install - caches locally the externals and the grid bundle


===============
Version v6r1p10
===============

WorloadManagement
=================

Bugfix
:::::::::::

 - JobAgent - set UseServerCertificate option "no" for the job executable


==============
Version v6r1p9
==============

Core
====

Bugfix
:::::::::::

 - dirac-configure - set the proper /DIRAC/Hostname when defining /LocalInstallation/Host

DataManagement
==============

Bugfix
:::::::::::

 - dirac-dms-user-lfns - fixed the case when the baseDir is specified
 - dirac-dms-remove-files - fixed crash in case of returned error report in a form of dictionary


==============
Version v6r1p8
==============

Web
===

Bugfix
:::::::::::

 - restored Run panel in the production monitor

Resources
=========

Bugfix
:::::::::::

 - FileCatalog - do not check existence of the catalog client module file


==============
Version v6r1p7
==============

Web
===

Bugfix
:::::::::::

 - fixed scroll bar in the Monitoring plots view


==============
Version v6r1p6
==============

Core
====

Bugfix
:::::::::::

 - TransferClient closes connections properly


==============
Version v6r1p5
==============

Core
====

Bugfix
:::::::::::

 - DISET Clients are now thread-safe. Same clients used twice in different threads was not closing the previous connection

Feature
::::::::::::

 - reduce wait times in DISET protocol machinery to improve performance


==============
Version v6r1p4
==============

RequestManagement
=================

Bugfix
:::::::::::

 - RequestContainer - in isSubRequestDone() treat special case for subrequests with files

Transformation
==============

Bugfix
:::::::::::

 - TransformationCleaningAgent - do not clear requests for tasks with no associated jobs


==============
Version v6r1p3
==============

Framework
=========

Bugfix
:::::::::::

 - Define the service location for the monitor
 - Close some connections that DISET was leaving open

Feature
::::::::::::

 - Pass the monitor down to the request RequestHandler


==============
Version v6r1p2
==============

WorkloadManagement
==================

Bugfix
:::::::::::

 - JobSchedulingAgent - use getSiteTiers() with returned direct value and not S_OK

Transformation
==============

Bugfix
:::::::::::

 - Uniform use of the TaskManager in the RequestTaskAgent and WorkflowTaskAgent


==============
Version v6r1p1
==============

RSS
===

Bugfix
:::::::::::

 - Alarm_PolType now really send mails instead of crashing silently.


============
Version v6r1
============

RSS
===

Bugfix
:::::::::::

 - ResourceStatusHandler - getStorageElementStatusWeb(), access mode by default is Read
 - RSS __init__.py will not crash anymore if no CS info provided
 - CS.getSiteTier now behaves correctly when a site is passed as a string

Change
:::::::::::

 - Major refactoring of the RSS system
 - DB.ResourceStatusDB has been refactored, making it a simple wrapper round ResourceStatusDB.sql with only four methods by table ( insert, update, get & delete )
 - DB.ResourceStatusDB.sql has been modified to support different statuses per granularity.
 - DB.ResourceManagementDB has been refactored, making it a simple wrapper round ResourceStatusDB.sql with only four methods by table ( insert, update, get & delete )
 - Service.ResourceStatusHandler has been refactored, removing all data processing, making it an intermediary between client and DB.
 - Service.ResourceManagementHandler has been refactored, removing all data processing, making it an intermediary between client and DB.
 - Client.ResourceStatusClient has been refactorerd. It connects automatically to DB or to the Service. Exposes DB and booster functions.
 - Client.ResourceManagementClient has been refactorerd. It connects automatically to DB or to the Service. Exposes DB and booster functions.
 - Agent.ClientsCacheFeederAgent renamed to CacheFeederAgent. The name was not accurate, as it also feeds Accouting Cache tables.
 - Agent.InspectorAgent, makes use of automatic API initialization.
 - Command. refactor and usage of automatic API initialization.
 - PolicySystem.PEP has reusable client connections, which increase significantly performance.
 - PolicySystem.PDP has reusable client connections, which increase significantly performance.
 - Utilities.Synchronizer syncs users and DIRAC sites
 - cosmetic changes everywhere, added HeadURL and RCSID
 - Removed all the VOExtension logic on RSS

Feature
::::::::::::

 - Utilities.ResourceStatusBooster makes use of the 'DB primitives' exposed on the client and does some useful data processing, exposing the new functions on the client.
 - Utilities.ResourceManagementBooster makes use of the 'DB primitives' exposed on the client and does some useful data processing, exposing the new functions on the client.
 - Utilities.Decorators are syntactic sugar for DB, Handler and Clients.
 - Utilities.MySQLMonkey is a mixture of laziness and refactoring, in order to generate the SQL statements automatically. Not anymore sqlStatemens hardcoded on the RSS.
 - Utilities.Validator are common checks done through RSS modules

dirac-setup-site
================

Bugfix
:::::::::::

 - fixed typos in the Script class name

Transformation
==============

Bugfix
:::::::::::

 - Missing logger in the TaskManager Client (was using agent's one)

Feature
::::::::::::

 - Added UnitTest class for TaskManager Client

DIRAC API
=========

Bugfix
:::::::::::

 - Dirac.py. If /LocalSite/FileCatalog is not define the default Catalog was not properly set.
 - Dirac.py - fixed __printOutput to properly interpret the first argument: 0:stdout, 1:stderr

Feature
::::::::::::

 - Dirac.py - added getConfigurationValue() method

Framework
=========

Feature
::::::::::::

 - UsersAndGroups agent to synchronize users from VOMRS server.

dirac-install
=============

Bugfix
:::::::::::

 - make Platform.py able to run with python2.3 to be used inside dirac-install
 - protection against the old or pro links pointing to non-existent directories
 - fixed the logic of creating links to /opt/dirac directories to take into account webRoot subdirs

Feature
::::::::::::

 - make use of the HTTP proxies if available

WorkloadManagement
==================

Bugfix
:::::::::::

 - SiteDirector - change getVO() function call to getVOForGroup()

Core:
=====

Bugfix
:::::::::::

 - Pfn.py - check the sanity of the pfn and catch the erroneous case

RequestManagement:
==================

Bugfix
:::::::::::

 - RequestContainer.isSubrequestDone() - return 0 if Done check fails

DataManagement
==============

Feature
::::::::::::

 - FileCatalog - possibility to configure multiple FileCatalog services of the same type


==============
Version v6r0p4
==============

Framework
=========

Bugfix
:::::::::::

 - Define the service location for the monitor
 - Close some connections that DISET was leaving open

Feature
::::::::::::

 - Pass the monitor down to the request RequestHandler


==============
Version v6r0p3
==============

Framework
=========

Bugfix
:::::::::::

 - ProxyManager - Registry.groupHasProperties() wasn't returning a result
 - typo dirac-proxy-info -> dirac-proxy-init in the expiration mail contents

Change
:::::::::::

 - Groups without AutoUploadProxy won't receive expiration notifications
 - DISET - directly close the connection after a failed handshake


==============
Version v6r0p2
==============

Framework
=========

Bugfix
:::::::::::

 - in services logs change ALWAYS log level for query messages to NOTICE


==============
Version v6r0p1
==============

Core
====

Bugfix
:::::::::::

 - List.uniqueElements() preserves the other of the remaining elements

Framework
=========

Bugfix
:::::::::::

 - Use all required arguments in read access data for UserProfileDB
 - NotificationClient - dropped LHCb-Production setup by default in the __getRPSClient()

Change
:::::::::::

 - By default set authorization rules to authenticated instead of all


============
Version v6r0
============

Framework
=========

Bugfix
:::::::::::

 - Never use the host certificate if there is one for dirac-proxy-init
 - ProxyManager - calculate properly the dates for credentials about to expire
 - Utilities/Security - hash VOMS Attributes as string
 - Utilities/Security - Generate a chain hash to discover if two chains are equal
 - SystemAdministrator - Do not set  a default lcg version

Change
:::::::::::

 - By default log level for agents and services is INFO
 - Disable the log headers by default before initializing
 - Proxy upload by default is one month with dirac-proxy-upload
 - ProxyManager will autoexpire old proxies, also auto purge logs
 - Rename dirac-proxy-upload to dirac-admin-proxy-upload
 - SecurityLogging - security log level to verbose
 - SysAdmin CLI - will try to connect to the service when setting the host

Feature
::::::::::::

 - DISET Framework modified client/server protocol, messaging mechanism to be used for optimizers
 - move functions in DIRAC.Core.Security.Misc to DIRAC.Core.Security.ProxyInfo
 - dirac-proxy-init modification according to issue #29: -U flag will upload a long lived proxy to the ProxyManager If /Registry/DefaultGroup is defined, try to generate a proxy that has that group Replaced params.debugMessage by gLogger.verbose. Closes #65 If AutoUploadProxy = true in the CS, the proxy will automatically be uploaded
 - Added upload of pilot proxies automatically
 - Print info after creating a proxy
 - Added setting VOMS extensions automatically
 - dirac-proxy-info can also print the information of the uploaded proxies
 - dirac-proxy-init will check that the lifetime of the certificate is less than one month and advise to renew it
 - dirac-proxy-init will check that the certificate has at least one month of validity
 - Proxy manager will send notifications when the uploaded proxies are about to expire (configurable via CS)
 - Now the proxyDB also has a knowledge of user names. Queries can use the user name as a query key
 - dirac-proxy-init will complain if the user certificate has less than 30 days
 - OracleDB - added Array type
 - MySQL - allow definition of the port number in the configuration
 - Use chain has to discover if it has already been dumped
 - SystemAdministrator - added Project support for the sysadmin
 - SysAdmin CLI - colorization of errors in the cli
 - Logger - added showing the thread id in the logger if enabled

Configuration
=============

Bugfix
:::::::::::

 - CE2CSAgent - update the CEType only if there is a relevant info in the BDII

Feature
::::::::::::

 - added getVOfromProxyGroup() utility
 - added getVoForGroup() utility, use it in the code as appropriate
 - added Registry and Operations Configuration helpers
 - dirac-configuration-shell - a configuration script for CS that behaves like an UNIX shellCHANGE: CSAPI - added more functionality required by updated configuration console
 - Added possibility to define LocalSE to any Site using the SiteLocalSEMapping section on the Operations Section
 - introduce Registry/VO section, associate groups to VOs, define SubmitPools per VO

ReleaseManagement
=================

Bugfix
:::::::::::

 - Install tools won't write HostDN to the configuration if the Admin username is not set
 - Properly set /DIRAC/Configuration/Servers when installing a CS Master
 - install_site.sh - missing option in wget for https download: --no-check-certificate
 - dirac-install-agent(service) - If the component being installed already has corresponding CS section, it is not overwritten unless explicitly asked for
 - dirac-install - define DYLD_LIBRARY_PATH ( for Mac installations )
 - dirac-install - Properly search for the LcgVer

Change
:::::::::::

 - dirac-install - write the defaults if any under defaults-.cfg so dirac-configure can pick it up
 - use new dirac_install from gothub/integration branch in install_site.sh

Feature
::::::::::::

 - release preparations and installation tools based on installation packages
 - dirac-compile-externals will try go get a DIRAC-free environment before compiling
 - dirac-disctribution - upload command can be defined via defaults file
 - dirac-disctribution - try to find if the version name is a branch or a tag in git and act accordingly
 - dirac-disctribution - added keyword substitution when creating a a distribution from git
 - dirac-install functionality enhancement: start using the switches as defined in issue #26;
 - dirac-install - put all the goodness under a function so scripts like lhcb-proxy-init can use it easily
 - dirac-install will write down the releases files in -d mode
 - Extensions can request custom external dependencies to be installed via pip when installing DIRAC.
 - LCG bundle version can be defined on a per release basis in the releases.cfg
 - dirac-deploy-scripts - when setting the lib path in the deploy scripts. Also search for subpaths of the libdir and include them
 - Install tools - plainly separate projects from installations

Accounting
==========

Bugfix
:::::::::::

 - Modified buckets width of 1week to 1 week + 1 day to fix summer time end week (1 hour more )

Change
:::::::::::

 - For the WMSHistory type, send as JobSplitType the JobType
 - Reduced the size of the max key length to workaround mysql max bytes for index problem

WorkloadManagement
==================

Bugfix
:::::::::::

 - SiteDirector - do not download pilot output if the flag getPilotOutput is not set
 - SSHTorque - retrieve job status by chunks of 100 jobs to avoid too long
 - JobDB - properly treat Site parameter in the job JDL while rescheduling jobs
 - PBSTimeLeft - proper handling of (p)cput parameter in the batch system output, recovery of the incomplete batch system output
 - ComputingElement - fixed proxy renewal logic for generic and private pilots
 - DownloadInputData - bug fixed in the naming of downloaded files
 - Matcher - set the group and DN when a request gets to the matcher if the request is not coming from a pilot
 - Matcher = take into account JobSharing when checking the owner for the request

Change
:::::::::::

 - SiteDirector - simplified executable generation
 - TimeLeft - call batch system commands with the ( default ) timeout 120 sec
 - PBSTimeLeft - uses default CPU/WallClock if not present in the output
 - PilotDirector, dirac-pilot - interpret -V flag of the pilot as Installation name

Feature
::::::::::::

 - SiteDirector - few more checks of error conditions
 - SiteDirector - limit the queue max length to the value of MaxQueueLengthOption ( 3 days be default )
 - JobDB will extract the VO when applying DIRAC/VOPolicy from the proper VO
 - glexecComputingElement - allow glexecComputingElement to "Reschedule" jobs if the Test of the glexec fails, instead of defaulting to InProcess. Controlled by RescheduleOnError Option of the glexecComputingElement
 - SandboxStore - create a different SBPath with the group included
 - JobSchedulingAgent - set the job Site attribute to the name of a group of sites corresponding to a SE chosen by the data staging procedure
 - automatically add SubmitPools JDL option of the job owner's VO defines it
 - JobManager - add MaxParametericJobs option to the service configuration
 - PilotDirector - each SubmitPool or Middleware can define TargetGrids
 - JobAgent - new StopOnApplicationFailure option to make the agent exiting the loop on application failure
 - PilotAgentsDB - on demand retrieval of the CREAM pilot output
 - Pilot - proper job ID evaluation for the OSG sites
 - JDL - added %j placeholder in the JDL to be replaced by the JobID

DataManagement
==============

Bugfix
:::::::::::

 - FileCatalog/DiractoryLevelTree - consistent application of the max directory level using global MAX_LEVELS variable
 - FileCatalog - Directory metadata is deleted together with the directory deletion, issue #40
 - LcgFileCatalog - use lfcthr and call lfcthr.init() to allow multithread try the import only once and just when LcgFileCatalogClient class is intantiated
 - StorageElement - get service CS options with getCSOption() method ( closes #97 )
 - retrieve FileCatalogs as ordered list, to have a proper default.
 - FileCatalog - bug fixes in the directory removal methods (closes #98)
 - RemovalAgent - TypeError when getting JobID in RemovalAgent
 - RemovalAgent - put a limit to be sure the execute method will end after a certain number of iterations
 - DownloadInputData - when files have been uploaded with lcg_util, the PFN filename might not match the LFN file name
 - putting FTSMonitor web page back

Change
:::::::::::

 - FileCatalog - the logic of the files query by metadata revisited to increase efficiency
 - FileCatalog - allow up to 15 levels of directories

Feature
::::::::::::

 - LcgFileCatalogClient - new version of getPathPermissions relying on the lfc_access method to solve the problem of multiple user DNs in LFC.
 - The default file catalog is now determined using /LocalSite/FileCatalog. The old behavior is provided as a fallback solution
 - ReplicaManager - can now deal with multiple catalogs. Makes sure the surl used for removal is the same as the one used for registration.
 - PoolXMLCatalog - added getTypeByPfn() function to get the type of the given PFN
 - dirac-dms-ban(allow)-se - added possibility to use CheckAccess property of the SE

StorageManagement
=================

Bugfix
:::::::::::

 - Stager - updateJobFromStager(): only return S_ERROR if the Status sent is not recognized or if a state update fails. If the jobs has been removed or has moved forward to another status, the Stager will get an S_OK and should forget about the job.
 - Requests older than 1 day, which haven't been staged are retried. Tasks older than "daysOld" number of days are set to Failed. These tasks have already been retried "daysOld" times for staging.
 - CacheReplicas and StageRequests records are kept until the pin has expired. This way the StageRequest agent will have proper accounting of the amount of staged data in cache.
 - Update Stager code in v6 to the same point as v5r13p37
 - StorageManager - avoid race condition by ensuring that Links=0 in the query while removing replicas

Feature
::::::::::::

 - new option in the StorageElement configuration "CheckAccess"
 - FTSCleaningAgent will allow to fix transient errors in RequestDB. At the moment it's only fixing Requests for which SourceTURL is equal to TargetSURL.
 - Stager - added new command dirac-stager-stage-files

RequestManagement
=================

Bugfix
:::::::::::

 - RequestDBFile - get request in chronological order (closes issue #84)
 - RequestDBFile - make getRequest return value for getRequest the same as for

ResourceStatusSystem
====================

Bugfix
:::::::::::

 - Cleaned RSS scripts, they are still prototypes

Change
:::::::::::

 - command caller looks on the extension for commands.
 - RSS use now the CS instead of getting info from Python modules.
 - PEP actions now reside in separate modules outside PEP module.
 - Updating various RSS tests to make them compatible with changes in the system.
 - Mostly trivial changes, typos, etc in various files in RSS
 - TokenAgent sends e-mails with current status

Feature
::::::::::::

 - Major code refacoring. First refactoring of RSS's PEP. Actions are now function defined in modules residing in directory "Actions".
 - methods to store cached environment on a DB and ge them.
 - RSS CS module add facilities to extract info from CS.
 - CS is used instead of ad-hoc configuration module in most places.
 - Adding various helper functions in RSS Utils module. These are functions used by RSS developers, including mainly myself, and are totally independant from the rest of DIRAC.

Transformation
==============

Bugfix
:::::::::::

 - TransformationDB - not removing task when site is not set
 - TransformationCleaningAgent - archiving instead of cleaning Removal and Replication transformations
 - TransformationCleaningAgent - kill jobs before deleting them

Change
:::::::::::

 - allow Target SE specification for jobs, Site parameter is not set in this case
 - TransformationAgent  - add new file statuses in production monitoring display
 - TransformationAgent - limit the number of files to be treated in TransformationAgent for replication and removal (default 5000)

Workflow
========

Feature
::::::::::::

 - allow modules to define Input and Output parameters that can be used instead of the step_commons/workflow_commons (Workflow.py, Step.py, Module.py)

Various fixes
=============

Bugfix
:::::::::::

 - Mail.py uses SMTP class rather than inheriting it
 - Platform utility will properly discover libc version even for the new Ubuntu
 - Removed old sandbox and other obsoleted components
