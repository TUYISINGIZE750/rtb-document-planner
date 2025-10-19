from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class SessionPlanBase(BaseModel):
    sector: Optional[str] = None
    sub_sector: Optional[str] = None
    trade: Optional[str] = None
    qualification_title: Optional[str] = None
    rqf_level: Optional[str] = None
    module_code_title: Optional[str] = None
    term: Optional[str] = None
    week: Optional[str] = None
    date: Optional[str] = None
    trainer_name: Optional[str] = None
    class_name: Optional[str] = None
    number_of_trainees: Optional[str] = None
    learning_outcomes: Optional[str] = None
    indicative_contents: Optional[str] = None
    topic_of_session: Optional[str] = None
    duration: Optional[str] = None
    objectives: Optional[str] = None
    facilitation_techniques: Optional[str] = None
    learning_activities: Optional[str] = None
    resources: Optional[str] = None
    assessment_details: Optional[str] = None
    references: Optional[str] = None
    appendices: Optional[str] = None
    reflection: Optional[str] = None
    session_range: Optional[str] = None

class SessionPlanCreate(SessionPlanBase):
    pass

class SessionPlanResponse(SessionPlanBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class SchemeOfWorkBase(BaseModel):
    # Institutional Information
    province: Optional[str] = None
    district: Optional[str] = None
    sector: Optional[str] = None
    school: Optional[str] = None
    department_trade: Optional[str] = None
    qualification_title: Optional[str] = None
    rqf_level: Optional[str] = None
    module_code_title: Optional[str] = None
    school_year: Optional[str] = None
    term: Optional[str] = None
    module_learning_hours: Optional[str] = None
    number_of_classes: Optional[str] = None
    class_name: Optional[str] = None
    cohort_size: Optional[str] = None
    trainer_name: Optional[str] = None
    trainer_position: Optional[str] = None
    
    terms: Optional[str] = None
    module_hours: Optional[str] = None
    
    # Module Overview
    module_rationale: Optional[str] = None
    entry_requirements: Optional[str] = None
    competency_codes: Optional[str] = None
    indicative_scope: Optional[str] = None
    standards_alignment: Optional[str] = None
    cross_cutting_issues: Optional[str] = None
    key_skills: Optional[str] = None
    delivery_approach: Optional[str] = None
    
    # Term 1
    term1_weeks: Optional[str] = None
    term1_learning_outcomes: Optional[str] = None
    term1_duration: Optional[str] = None
    term1_indicative_contents: Optional[str] = None
    term1_activities: Optional[str] = None
    term1_resources: Optional[str] = None
    term1_assessment: Optional[str] = None
    term1_place: Optional[str] = None
    
    # Term 2
    term2_weeks: Optional[str] = None
    term2_learning_outcomes: Optional[str] = None
    term2_duration: Optional[str] = None
    term2_indicative_contents: Optional[str] = None
    term2_activities: Optional[str] = None
    term2_resources: Optional[str] = None
    term2_assessment: Optional[str] = None
    term2_place: Optional[str] = None
    
    # Term 3
    term3_weeks: Optional[str] = None
    term3_learning_outcomes: Optional[str] = None
    term3_duration: Optional[str] = None
    term3_indicative_contents: Optional[str] = None
    term3_activities: Optional[str] = None
    term3_resources: Optional[str] = None
    term3_assessment: Optional[str] = None
    term3_place: Optional[str] = None
    
    # Assessment
    formative_assessment: Optional[str] = None
    summative_assessment: Optional[str] = None
    resource_inventory: Optional[str] = None
    health_safety: Optional[str] = None
    
    # Sign-offs
    dos_name: Optional[str] = None
    manager_name: Optional[str] = None

class SchemeOfWorkCreate(SchemeOfWorkBase):
    # Simplified for backward compatibility
    learning_outcomes: Optional[str] = None
    indicative_contents: Optional[str] = None
    learning_activities: Optional[str] = None
    resources: Optional[str] = None
    evidence_of_assessment: Optional[str] = None
    learning_place: Optional[str] = None
    weeks_covered: Optional[str] = None

class SchemeOfWorkResponse(SchemeOfWorkBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True