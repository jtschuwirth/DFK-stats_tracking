from dfk_commons.classes.TablesManager import TablesManager

def getQuestingUptimeByProfession(tablesManager: TablesManager, profession: str):

    allAccounts = tablesManager.accounts.scan(
        FilterExpression="enabled_quester=:enabled_quester AND profession=:profession",
        ExpressionAttributeValues={
            ":enabled_quester": True,
            ":profession": profession
        }
    )["Items"]
    questingAccounts = tablesManager.accounts.scan(
        FilterExpression="questing=:questing AND profession=:profession",
        ExpressionAttributeValues={
            ":questing": True,
            ":profession": profession
        }
    )["Items"]
   
    if len(allAccounts) == 0:
       return 0
    return len(questingAccounts)/len(allAccounts)