# CreateUpdateApiSchemaFileRequest

Information about schema file.

**Properties**

| Name    | Type                          | Required | Description                                                                                 |
| :------ | :---------------------------- | :------- | :------------------------------------------------------------------------------------------ |
| name    | str                           | ❌       | The schema file's name.                                                                     |
| root    | CreateUpdateApiSchemaFileRoot | ❌       | Information about the schema's root file. This tag only applies to protobuf specifications. |
| content | str                           | ❌       | The schema file's content.                                                                  |

# CreateUpdateApiSchemaFileRoot

Information about the schema's root file. This tag only applies to protobuf specifications.

**Properties**

| Name    | Type | Required | Description                             |
| :------ | :--- | :------- | :-------------------------------------- |
| enabled | bool | ❌       | If true, tag the file as the root file. |

<!-- This file was generated by liblab | https://liblab.com/ -->
