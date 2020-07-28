# create covert action types
db.session.add(CovertActionType(
    requested_action = "Background check",
    category = "Intel gathering",
    description = "A desktop exercise in which an agent trawls publicly available information on a subject to build a profile of their life, career, motivations and views of the regime",
    approval_level_required = 2,
    work_credits_required = 2))

db.session.add(CovertActionType(
    requested_action = "Tail",
    category = "Intel gathering",
    description = "A Covert Ops team is tasked with following the subject, identifying their behaviour, relationships and travel",
    approval_level_required = 2,
    work_credits_required = 4))

db.session.add(CovertActionType(
    requested_action = "Hack phone", # Suggestion: perhaps instead of hack phone, it could be wiretappig? Would allow the description to be used to intercept e-mail comms as well.
    category = "Intel gathering",
    description = "Use covert methods to gain access to to the subject's mobile phone calls and texts",
    approval_level_required = 2,
    work_credits_required = 5))

db.session.add(CovertActionType(
    requested_action = "Trawl bank records",
    category = "Intel gathering",
    description = "Gain access to a subject's banking records, allowing identification of spending patterns, wealth and unexplained behaviour",
    approval_level_required = 2,
    work_credits_required = 5))

db.session.add(CovertActionType(
    requested_action = "Kidnap and interrogate",
    category = "Direct action",
    description = "This will yield extensive intelligence on a subject. We will impersonate agents of the regime, so it will also weaken the subject's loyalty to the regime",
    approval_level_required = 5,
    work_credits_required = 15))

db.session.add(CovertActionType(
    requested_action = "Honeypot",
    category = "Establish vulnerability",
    description = "Task a Covert Ops operative with special skills to seduce the target: can lead to information as well as blackmail leverage",
    approval_level_required = 3,
    work_credits_required = 10))

db.session.add(CovertActionType(
    requested_action = "Remove",
    category = "Direct action",
    description = "Remove a threat permanently",
    approval_level_required = 5,
    work_credits_required = 40))

#############
# Suggestions
#############
#
# Incrimination (Vulnerability) == the idea is to create a blackmail against the target utilising more crime-related blackmail, e.g. planted photos, fake paper trails, etc.
# requested_action = "Incrimination",
# category = "Establish vulnerability",
# description = "Create falsified evidence incriminating the target in an illegal act in order to gain leverage over the target",
# approval_level_required = 3?,
# work_credits_required = 10?
#
# Brainwashing (Direct Action) == reprogram the target's allegiance and instantly recruit the target, but the chances of being burnt/exposed is high
# requested_action = "Brainwashing",
# category = "Direct action",
# description = "Using a mix of hypno-theraphy and experimental drugs, the target will be bent into our unwitting tool",
# approval_level_required = 5?,
# work_credits_required = 80?
#
# Disinformation campaign (Vulnerability/direct action?) == whereas other action seeks to find blackmail, this action reduces the target's loyalty to the regime
# requested_action = "Disinformation campaign",
# category = "Establish vulnerability" / "Direct action", # Depends on which one you'd think fit best
# description = "The target will be bombarded by a series of targeted anti-regime ads and fake news to lower their loyalty to the regime",
# approval_level_required = 3?,
# work_credits_required = 10?
#
# Harrasment (Vulnerability/direct action?) == attempts to reduce the target's loyalty to the regime, while at the same time increasing fear of the agency
# requested_action = "Harrasment"
# category = "Direct action", # Depends on which one you'd think fit best
# description = "The target will be harassed physically and electronically, culminating with a few fake bomb threats, designed to instill fear onto the target",
# approval_level_required = 5?,
# work_credits_required = 20?
#
# Financial sabotage (Establish vulnerability) == target's finances is disrupted, creating the potential for financially-connected blackmail (in debt/gambling/stealing from employer) and perhaps allowing agents to gain some extra cash
# requested_action = "Financial sabotage",
# category = "Establish vulnerability",
# description = "A Coverts Ops team will be dispatched to strip the targets' wealth and assets which could lead the target into performing financial-related crimes",
# approval_level_required = 3?,
# work_credits_required = 15?
#
# Pay informants (Intel gathering) == perhaps an idea for the future, but allow agents to use cash to buy off info about the target; would require recruited sources first
# requested_action = "Pay informants",
# category = "Intel gathering",
# description = "Covert Ops will pay a visit to several local informants to purchase information about the target",
# approval_level_required = 2?,
# work_credits_required = 2?
# Would reduce cash by about $2000
#
# Smear campaigns (Direct action) == reduces the target's loyalty to the regime, though have the potential to demote the target's intel value?
# requested_action = "Smear campaigns",
# category = "Direct action",
# description = "Nasty rumors about the target will be spread to every news outlet and tabloid columns in the country, causing psychological harm to the target",
# approval_level_required = 5?,
# work_credits_required = 15?
#
# Personal disruptions (Direct action) == increases the target's fear of the agency, though would potentially increase the target's loyalty to the regime"
# requested_action = "Personal disruptions"
# category = "Direct action",
# description = "Mislabelled medicines, property damages, and sabotages: these minor things will slowly demoralize the target",
# approval_level_required = 5?,
# work_credits_required = 20?
