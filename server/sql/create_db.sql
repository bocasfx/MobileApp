BEGIN TRANSACTION;
CREATE TABLE init(id NONE);
CREATE TABLE JOB ( ID VARCHAR2 NOT NULL, NAME VARCHAR2 NOT NULL, DESCRIPTION VARCHAR2 NOT NULL, PARENT_JOB_ID VARCHAR2 NOT NULL, SCOPE_ID VARCHAR2 NOT NULL);
INSERT INTO [JOB] ([ID], [NAME], [DESCRIPTION], [PARENT_JOB_ID], [SCOPE_ID]) VALUES ('F62F279D-D23A-4B8B-41FA-7F3E407880FA', 'IMPORT', 'Import to cluster repository: Agility_Solution 1.770.TRUNK.b00.20130710 win32-ix86', 'ROOT', '91A1D0AC-5E92-4EBD-75DC-624A4C257E25');
INSERT INTO [JOB] ([ID], [NAME], [DESCRIPTION], [PARENT_JOB_ID], [SCOPE_ID]) VALUES ('5F2CDB57-133C-4AA0-6C44-3F6E4B411000', 'IMPORT', 'Import to cluster repository: Agility_Solution 1.770.TRUNK.b00.20130710 win32-ix86', 'ROOT', '91A1D0AC-5E92-4EBD-75DC-624A4C257E25');
INSERT INTO [JOB] ([ID], [NAME], [DESCRIPTION], [PARENT_JOB_ID], [SCOPE_ID]) VALUES ('CC3E073F-B341-40EA-571D-CF2067D9CE2A', 'DEPLOY', 'Deploy209', 'ROOT', '00D59058-34FB-4B1F-6533-CE0DF22BACDE');
INSERT INTO [JOB] ([ID], [NAME], [DESCRIPTION], [PARENT_JOB_ID], [SCOPE_ID]) VALUES ('29C27CE4-CD10-4B95-6440-E946169C69F3', 'deliver', 'deliver Agility_Solution 1.770.TRUNK.b00.20130710 to Impax Agility', 'CC3E073F-B341-40EA-571D-CF2067D9CE2A', '00D59058-34FB-4B1F-6533-CE0DF22BACDE');
INSERT INTO [JOB] ([ID], [NAME], [DESCRIPTION], [PARENT_JOB_ID], [SCOPE_ID]) VALUES ('4A54DCF0-C5D1-4744-73D1-D5828AE5DBE9', 'minint-r6cn2kl', 'minint-r6cn2kl', '29C27CE4-CD10-4B95-6440-E946169C69F3', '00D59058-34FB-4B1F-6533-CE0DF22BACDE');
INSERT INTO [JOB] ([ID], [NAME], [DESCRIPTION], [PARENT_JOB_ID], [SCOPE_ID]) VALUES ('8CF4206B-82BB-406D-6B11-A13A96CC240F', 'minint-0eir1aj', 'minint-0eir1aj', '29C27CE4-CD10-4B95-6440-E946169C69F3', '00D59058-34FB-4B1F-6533-CE0DF22BACDE');
INSERT INTO [JOB] ([ID], [NAME], [DESCRIPTION], [PARENT_JOB_ID], [SCOPE_ID]) VALUES ('5585B8F8-3848-4BFE-5AEF-D642FAD714DE', 'configure', 'configure Agility_Solution 1.770.TRUNK.b00.20130710 on Impax Agility', 'CC3E073F-B341-40EA-571D-CF2067D9CE2A', '00D59058-34FB-4B1F-6533-CE0DF22BACDE');
INSERT INTO [JOB] ([ID], [NAME], [DESCRIPTION], [PARENT_JOB_ID], [SCOPE_ID]) VALUES ('A102489F-D038-43EC-4817-80B301B7DBCF', 'minint-r6cn2kl', 'minint-r6cn2kl', '5585B8F8-3848-4BFE-5AEF-D642FAD714DE', '00D59058-34FB-4B1F-6533-CE0DF22BACDE');
INSERT INTO [JOB] ([ID], [NAME], [DESCRIPTION], [PARENT_JOB_ID], [SCOPE_ID]) VALUES ('5AD1CC4E-1DA0-4869-75D6-4FD18BE50988', 'minint-0eir1aj', 'minint-0eir1aj', '5585B8F8-3848-4BFE-5AEF-D642FAD714DE', '00D59058-34FB-4B1F-6533-CE0DF22BACDE');
INSERT INTO [JOB] ([ID], [NAME], [DESCRIPTION], [PARENT_JOB_ID], [SCOPE_ID]) VALUES ('25C7F1F0-B571-4C09-5332-7382B2F32499', 'validate', 'validate Agility_Solution 1.770.TRUNK.b00.20130710 on Impax Agility', 'CC3E073F-B341-40EA-571D-CF2067D9CE2A', '00D59058-34FB-4B1F-6533-CE0DF22BACDE');
INSERT INTO [JOB] ([ID], [NAME], [DESCRIPTION], [PARENT_JOB_ID], [SCOPE_ID]) VALUES ('C74C78CA-79F7-44C9-402F-E63BB411CE90', 'minint-r6cn2kl', 'minint-r6cn2kl', '25C7F1F0-B571-4C09-5332-7382B2F32499', '00D59058-34FB-4B1F-6533-CE0DF22BACDE');
INSERT INTO [JOB] ([ID], [NAME], [DESCRIPTION], [PARENT_JOB_ID], [SCOPE_ID]) VALUES ('FC494D7E-2583-4DA0-6493-DD0C63AC9B2D', 'minint-0eir1aj', 'minint-0eir1aj', '25C7F1F0-B571-4C09-5332-7382B2F32499', '00D59058-34FB-4B1F-6533-CE0DF22BACDE');
INSERT INTO [JOB] ([ID], [NAME], [DESCRIPTION], [PARENT_JOB_ID], [SCOPE_ID]) VALUES ('A92B0435-1639-4BA5-7F19-537F4EF710FE', 'deliver', 'deliver Agility_Solution 1.770.TRUNK.b00.20130710 to Impax Agility', 'CC3E073F-B341-40EA-571D-CF2067D9CE2A', '00D59058-34FB-4B1F-6533-CE0DF22BACDE');
INSERT INTO [JOB] ([ID], [NAME], [DESCRIPTION], [PARENT_JOB_ID], [SCOPE_ID]) VALUES ('9791F776-AC1F-4395-6598-D7CEF3D7EE60', 'configure', 'configure Agility_Solution 1.770.TRUNK.b00.20130710 on Impax Agility', 'CC3E073F-B341-40EA-571D-CF2067D9CE2A', '00D59058-34FB-4B1F-6533-CE0DF22BACDE');
INSERT INTO [JOB] ([ID], [NAME], [DESCRIPTION], [PARENT_JOB_ID], [SCOPE_ID]) VALUES ('E4943FA1-F103-4077-4A14-96548503AF4C', 'minint-r6cn2kl', 'minint-r6cn2kl', '9791F776-AC1F-4395-6598-D7CEF3D7EE60', '00D59058-34FB-4B1F-6533-CE0DF22BACDE');
INSERT INTO [JOB] ([ID], [NAME], [DESCRIPTION], [PARENT_JOB_ID], [SCOPE_ID]) VALUES ('4325229C-E1CB-4B1C-41DA-AAD1E274E7A2', 'minint-0eir1aj', 'minint-0eir1aj', '9791F776-AC1F-4395-6598-D7CEF3D7EE60', '00D59058-34FB-4B1F-6533-CE0DF22BACDE');
INSERT INTO [JOB] ([ID], [NAME], [DESCRIPTION], [PARENT_JOB_ID], [SCOPE_ID]) VALUES ('61AE3116-BFB3-49A7-6941-DC788C88707D', 'validate', 'validate Agility_Solution 1.770.TRUNK.b00.20130710 on Impax Agility', 'CC3E073F-B341-40EA-571D-CF2067D9CE2A', '00D59058-34FB-4B1F-6533-CE0DF22BACDE');
INSERT INTO [JOB] ([ID], [NAME], [DESCRIPTION], [PARENT_JOB_ID], [SCOPE_ID]) VALUES ('FB49ED31-4696-43A0-6BE2-FAF82A48E22A', 'minint-r6cn2kl', 'minint-r6cn2kl', '61AE3116-BFB3-49A7-6941-DC788C88707D', '00D59058-34FB-4B1F-6533-CE0DF22BACDE');
INSERT INTO [JOB] ([ID], [NAME], [DESCRIPTION], [PARENT_JOB_ID], [SCOPE_ID]) VALUES ('CB38E5BD-AE84-4302-449F-7439798F8C24', 'minint-0eir1aj', 'minint-0eir1aj', '61AE3116-BFB3-49A7-6941-DC788C88707D', '00D59058-34FB-4B1F-6533-CE0DF22BACDE');
INSERT INTO [JOB] ([ID], [NAME], [DESCRIPTION], [PARENT_JOB_ID], [SCOPE_ID]) VALUES ('846618CC-BC49-4479-6B95-6AC89939E1E8', 'INSTALL', 'INSTALL Agility_Solution 1.770.TRUNK.b00.20130710 on all', 'CC3E073F-B341-40EA-571D-CF2067D9CE2A', '00D59058-34FB-4B1F-6533-CE0DF22BACDE');
INSERT INTO [JOB] ([ID], [NAME], [DESCRIPTION], [PARENT_JOB_ID], [SCOPE_ID]) VALUES ('44FE5510-9B39-471B-5F72-9A89E0B3F3F8', 'minint-r6cn2kl', 'minint-r6cn2kl', '846618CC-BC49-4479-6B95-6AC89939E1E8', '00D59058-34FB-4B1F-6533-CE0DF22BACDE');
INSERT INTO [JOB] ([ID], [NAME], [DESCRIPTION], [PARENT_JOB_ID], [SCOPE_ID]) VALUES ('D6F84D91-3D81-4FED-7DD9-7377A332EDCA', 'minint-0eir1aj', 'minint-0eir1aj', '846618CC-BC49-4479-6B95-6AC89939E1E8', '00D59058-34FB-4B1F-6533-CE0DF22BACDE');
INSERT INTO [JOB] ([ID], [NAME], [DESCRIPTION], [PARENT_JOB_ID], [SCOPE_ID]) VALUES ('544B6D00-148B-401C-7285-9BF50BF423BC', 'START', 'Start311', 'ROOT', '00D59058-34FB-4B1F-6533-CE0DF22BACDE');
INSERT INTO [JOB] ([ID], [NAME], [DESCRIPTION], [PARENT_JOB_ID], [SCOPE_ID]) VALUES ('F32D2AE7-168B-458F-7F4C-448207F4D0CC', 'start', 'START Agility_Solution [new] on all', '544B6D00-148B-401C-7285-9BF50BF423BC', '00D59058-34FB-4B1F-6533-CE0DF22BACDE');
INSERT INTO [JOB] ([ID], [NAME], [DESCRIPTION], [PARENT_JOB_ID], [SCOPE_ID]) VALUES ('A94662DF-225B-4876-4BC3-DF25CA146661', '1.770.TRUNK.b00.20130710', '1.770.TRUNK.b00.20130710', 'F32D2AE7-168B-458F-7F4C-448207F4D0CC', '00D59058-34FB-4B1F-6533-CE0DF22BACDE');
INSERT INTO [JOB] ([ID], [NAME], [DESCRIPTION], [PARENT_JOB_ID], [SCOPE_ID]) VALUES ('3E4AFFAA-E10C-42FF-45D8-50D87BAE0027', 'minint-r6cn2kl', 'minint-r6cn2kl', 'A94662DF-225B-4876-4BC3-DF25CA146661', '00D59058-34FB-4B1F-6533-CE0DF22BACDE');
INSERT INTO [JOB] ([ID], [NAME], [DESCRIPTION], [PARENT_JOB_ID], [SCOPE_ID]) VALUES ('0E0E54DC-D6D8-4E88-5D63-234EF2D4D6B0', '1.770.TRUNK.b00.20130710', '1.770.TRUNK.b00.20130710', 'F32D2AE7-168B-458F-7F4C-448207F4D0CC', '00D59058-34FB-4B1F-6533-CE0DF22BACDE');
INSERT INTO [JOB] ([ID], [NAME], [DESCRIPTION], [PARENT_JOB_ID], [SCOPE_ID]) VALUES ('2344EEE8-25B6-486C-7495-12685B3C1EB4', 'minint-0eir1aj', 'minint-0eir1aj', '0E0E54DC-D6D8-4E88-5D63-234EF2D4D6B0', '00D59058-34FB-4B1F-6533-CE0DF22BACDE');
INSERT INTO [JOB] ([ID], [NAME], [DESCRIPTION], [PARENT_JOB_ID], [SCOPE_ID]) VALUES ('58811561-1699-4789-41BF-6F25776A9303', 'STOP', 'Stop333', 'ROOT', '00D59058-34FB-4B1F-6533-CE0DF22BACDE');
INSERT INTO [JOB] ([ID], [NAME], [DESCRIPTION], [PARENT_JOB_ID], [SCOPE_ID]) VALUES ('AFA2A022-721B-4FA7-7810-A291CC27C5AD', 'stop', 'STOP Agility_Solution [new] on all', '58811561-1699-4789-41BF-6F25776A9303', '00D59058-34FB-4B1F-6533-CE0DF22BACDE');
INSERT INTO [JOB] ([ID], [NAME], [DESCRIPTION], [PARENT_JOB_ID], [SCOPE_ID]) VALUES ('3C23373B-0840-4C0F-4C85-82793A85C419', '1.770.TRUNK.b00.20130710', '1.770.TRUNK.b00.20130710', 'AFA2A022-721B-4FA7-7810-A291CC27C5AD', '00D59058-34FB-4B1F-6533-CE0DF22BACDE');
INSERT INTO [JOB] ([ID], [NAME], [DESCRIPTION], [PARENT_JOB_ID], [SCOPE_ID]) VALUES ('4C13A759-6654-4081-5BED-F0909F48619B', 'minint-r6cn2kl', 'minint-r6cn2kl', '3C23373B-0840-4C0F-4C85-82793A85C419', '00D59058-34FB-4B1F-6533-CE0DF22BACDE');
INSERT INTO [JOB] ([ID], [NAME], [DESCRIPTION], [PARENT_JOB_ID], [SCOPE_ID]) VALUES ('16832DA5-2F81-4F04-7B67-55D5D255C4DE', '1.770.TRUNK.b00.20130710', '1.770.TRUNK.b00.20130710', 'AFA2A022-721B-4FA7-7810-A291CC27C5AD', '00D59058-34FB-4B1F-6533-CE0DF22BACDE');
INSERT INTO [JOB] ([ID], [NAME], [DESCRIPTION], [PARENT_JOB_ID], [SCOPE_ID]) VALUES ('678ADACC-6EE8-48C5-65B6-10BE383585BB', 'minint-0eir1aj', 'minint-0eir1aj', '16832DA5-2F81-4F04-7B67-55D5D255C4DE', '00D59058-34FB-4B1F-6533-CE0DF22BACDE');