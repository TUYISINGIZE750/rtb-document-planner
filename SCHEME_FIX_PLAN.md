# Scheme of Work Fix Plan

## Issues to Fix:

1. **Missing Info Table** - Need to add table with:
   - Sector / Trainer
   - Trade / School Year
   - Qualification Title / Term
   - RQF Level / Module details
   - Module code and title
   - Learning hours
   - Number of Classes
   - Date / Class Name

2. **Term 1 Not Formatted Like Terms 2 & 3** - Already fixed (light green headers + bold)

3. **Missing Signature Table** - Need to add at end:
   - Prepared by: (Name, position and Signature) TRAINER
   - Verified by: (Name, position and Signature) DOS
   - Approved by: (Name, position and Signature) SCHOOL MANAGER

## Current Structure:
- Table 0: School Header (added by code)
- Table 1: Term 1 (from template)
- Table 2: Terms 2 & 3 (from template)

## Required Structure:
- Table 0: School Header (already added)
- **Table 1: INFO TABLE (NEED TO ADD)**
- Table 2: Term 1 (from template)
- Table 3: Terms 2 & 3 (from template)
- **Table 4: SIGNATURE TABLE (NEED TO ADD)**

## Solution:
1. After adding school header, INSERT info table
2. Keep all existing term table logic
3. At the end, ADD signature table

This will NOT break existing logic - just adds tables before and after.
