def build_incident_prompt(incident):

    return f"""
You are an expert Network Operations Engineer.

Analyze this incident.

Incident Number:
{incident.incident_number}

Store:
{incident.store_id}

Short Description:
{incident.short_description}

Description:
{incident.description}

Priority:
{incident.priority}

Generate:

1. Executive Summary

2. Possible Root Causes

3. Troubleshooting Steps

4. Work Notes

5. Whether Vendor Escalation is Required

Respond professionally.
"""