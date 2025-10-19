from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database import Base
import json

class SessionPlan(Base):
    __tablename__ = "session_plans"

    id = Column(Integer, primary_key=True, index=True)
    sector = Column(String(255))
    sub_sector = Column(String(255))
    trade = Column(String(255))
    qualification_title = Column(String(500))
    rqf_level = Column(String(50))
    module_code_title = Column(String(500))
    term = Column(String(100))
    week = Column(String(100))
    date = Column(String(100))
    trainer_name = Column(String(255))
    class_name = Column(String(255))
    number_of_trainees = Column(String(100))
    learning_outcomes = Column(Text)
    indicative_contents = Column(Text)
    topic_of_session = Column(String(500))
    duration = Column(String(100))
    objectives = Column(Text)
    facilitation_techniques = Column(Text)
    learning_activities = Column(Text)
    resources = Column(Text)
    assessment_details = Column(Text)
    references = Column(Text)
    appendices = Column(Text)
    reflection = Column(Text)
    session_range = Column('session_range', Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class SchemeOfWork(Base):
    __tablename__ = "schemes_of_work"

    id = Column(Integer, primary_key=True, index=True)
    # Institutional
    province = Column(String(255))
    district = Column(String(255))
    sector = Column(String(255))
    school = Column(String(255))
    department_trade = Column(String(255))
    qualification_title = Column(String(500))
    rqf_level = Column(String(50))
    module_code_title = Column(String(500))
    school_year = Column(String(100))
    term = Column(String(100))
    module_learning_hours = Column(String(100))
    number_of_classes = Column(String(100))
    class_name = Column(String(255))
    cohort_size = Column(String(100))
    trainer_name = Column(String(255))
    trainer_position = Column(String(255))
    
    # Module Overview
    module_rationale = Column(Text)
    entry_requirements = Column(Text)
    competency_codes = Column(Text)
    indicative_scope = Column(Text)
    standards_alignment = Column(Text)
    cross_cutting_issues = Column(Text)
    key_skills = Column(Text)
    delivery_approach = Column(Text)
    
    # Assessment
    formative_assessment = Column(Text)
    summative_assessment = Column(Text)
    resource_inventory = Column(Text)
    health_safety = Column(Text)
    
    # Additional fields
    terms = Column(String(255))
    module_hours = Column(String(100))
    
    # Term data (JSON strings)
    term1_weeks = Column(Text)
    term1_learning_outcomes = Column(Text)
    term1_indicative_contents = Column(Text)
    term1_duration = Column(Text)
    term1_activities = Column(Text)
    term1_resources = Column(Text)
    term1_assessment = Column(Text)
    term1_place = Column(Text)
    
    term2_weeks = Column(Text)
    term2_learning_outcomes = Column(Text)
    term2_indicative_contents = Column(Text)
    term2_duration = Column(Text)
    term2_activities = Column(Text)
    term2_resources = Column(Text)
    term2_assessment = Column(Text)
    term2_place = Column(Text)
    
    term3_weeks = Column(Text)
    term3_learning_outcomes = Column(Text)
    term3_indicative_contents = Column(Text)
    term3_duration = Column(Text)
    term3_activities = Column(Text)
    term3_resources = Column(Text)
    term3_assessment = Column(Text)
    term3_place = Column(Text)
    
    # Sign-offs
    dos_name = Column(String(255))
    manager_name = Column(String(255))
    
    # Legacy fields for backward compatibility
    sub_sector = Column(String(255))
    trade = Column(String(255))
    weeks_covered = Column(String(200))
    learning_outcomes = Column(Text)
    indicative_contents = Column(Text)
    learning_activities = Column(Text)
    resources = Column(Text)
    evidence_of_assessment = Column(Text)
    learning_place = Column(String(255))
    observation_notes = Column(Text)
    integrated_assessment = Column(Text)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(255), unique=True, index=True)
    name = Column(String(255), nullable=False)
    phone = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(255))
    institution = Column(String(255))
    password = Column(String(255), nullable=False)
    role = Column(String(50), default='user')
    is_premium = Column(Boolean, default=False)
    session_plans_limit = Column(Integer, default=2)
    schemes_limit = Column(Integer, default=2)
    session_plans_downloaded = Column(Integer, default=0)
    schemes_downloaded = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    notifications = relationship("Notification", back_populates="user")

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String(255), nullable=False)
    message = Column(Text, nullable=False)
    type = Column(String(50), default='info')  # info, success, warning, error
    is_read = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationship
    user = relationship("User", back_populates="notifications")

class Settings(Base):
    __tablename__ = "settings"

    id = Column(Integer, primary_key=True, index=True)
    key = Column(String(255), unique=True, nullable=False)
    value = Column(String(255), nullable=False)
    description = Column(String(500))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())