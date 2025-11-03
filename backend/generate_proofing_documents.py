"""Generate proof-reading documents for final verification before going live"""
import sys
import os
from datetime import datetime

# Add backend to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from official_template_filler import fill_session_plan_official, fill_scheme_official

print("=" * 80)
print("GENERATING PROOF-READING DOCUMENTS")
print("=" * 80)
print()

# ============================================================================
# 1. SESSION PLAN - Comprehensive realistic example
# ============================================================================
print("1. Generating Session Plan...")
session_data = {
    'school_name': 'IPRC Kigali',
    'province': 'Kigali City',
    'district': 'Gasabo',
    'sector_location': 'Remera',
    'cell': 'Rukiri I',
    'village': 'Amahoro',
    'school_logo': '',
    
    'sector': 'ICT',
    'trade': 'Computer System Administration',
    'level': 'Level 5',
    'date': '15/01/2025',
    'trainer_name': 'MUGISHA Jean Paul',
    'school_year': '2024-2025',
    'term': 'Term 2',
    'module_code_title': 'CSA-M05: Network Administration and Security',
    'week': '3',
    'number_of_trainees': '28',
    'class_name': 'L5CSA-A',
    
    'learning_outcomes': 'Configure and secure network infrastructure\nImplement firewall rules and access control lists\nMonitor network traffic and identify security threats',
    
    'indicative_contents': 'Network security fundamentals\nFirewall configuration (iptables, pfSense)\nVPN setup and management\nIntrusion detection systems\nNetwork monitoring tools',
    
    'topic_of_session': 'Configuring Firewall Rules and Access Control Lists',
    'range': 'Network Security Module',
    'duration': '3 hours (180 minutes)',
    
    'objectives': '''1. Understand firewall architecture and packet filtering concepts
2. Configure basic firewall rules using iptables
3. Create and implement access control lists (ACLs)
4. Test firewall rules and verify network security
5. Document firewall configurations and security policies''',
    
    'facilitation_techniques': 'Demonstration, Hands-on practice, Group work, Problem-solving',
    
    'learning_activities': '''Introduction:
Review previous lesson on network security basics. Introduce firewall concepts and demonstrate real-world firewall scenarios. Discuss the importance of proper firewall configuration in protecting network infrastructure.

Development:
Step 1: Demonstrate firewall architecture and packet filtering process using diagrams and live examples.
Step 2: Guide trainees through installing and configuring iptables on Linux systems.
Step 3: Show how to create basic firewall rules (INPUT, OUTPUT, FORWARD chains).
Step 4: Demonstrate creating access control lists for different network segments.
Step 5: Practice testing firewall rules using various network tools (ping, telnet, nmap).

Conclusion:
Summarize key firewall configuration concepts. Review common mistakes and best practices. Assign homework to configure a complete firewall solution for a small business network.''',
    
    'resources': '''Linux servers (Ubuntu/CentOS)
Network simulation software (GNS3 or Packet Tracer)
Firewall documentation and reference guides
Network testing tools (nmap, wireshark)
Whiteboard and markers
Projector and presentation slides''',
    
    'assessment_details': '''Practical assessment: Configure firewall rules for given network scenario
Observation: Monitor trainees during hands-on practice
Written test: Answer questions on firewall concepts and ACL syntax
Group presentation: Present firewall security policy for case study''',
    
    'evaluation': 'Trainer self-assessment form, Trainee feedback survey',
    
    'references': '''1. "Linux Firewalls: Attack Detection and Response" by Michael Rash
2. Netfilter/iptables official documentation (netfilter.org)
3. SANS Institute - Firewall Configuration Best Practices
4. CompTIA Security+ Study Guide, Chapter 5: Network Security''',
    
    'appendix': '''PowerPoint presentation: Firewall Architecture
Lab worksheet: iptables Configuration Exercise
Assessment rubric: Firewall Configuration Project
Network topology diagram for practice scenarios'''
}

try:
    session_file = fill_session_plan_official(session_data)
    final_session = os.path.join(os.path.dirname(__file__), 'PROOFING_Session_Plan.docx')
    
    import shutil
    shutil.copy(session_file, final_session)
    
    size = os.path.getsize(final_session)
    print(f"   SUCCESS: Session Plan generated: {size:,} bytes")
    print(f"   Location: {final_session}")
except Exception as e:
    print(f"   ERROR: {e}")
    import traceback
    traceback.print_exc()

print()

# ============================================================================
# 2. SCHEME OF WORK - Comprehensive realistic example
# ============================================================================
print("2. Generating Scheme of Work...")
scheme_data = {
    'school_name': 'IPRC Huye',
    'province': 'Amajyepfo',
    'district': 'Huye',
    'sector_location': 'Ngoma',
    'cell': 'Matyazo',
    'village': 'Karama',
    'school_logo': '',
    
    'sector': 'Construction',
    'trade': 'Building Construction',
    'trainer_name': 'NIYONZIMA Patrick',
    'school_year': '2024-2025',
    'terms': 'Term 1, 2, 3',
    'qualification_title': 'Advanced Diploma in Building Construction',
    'rqf_level': 'Level 6',
    'module_code_title': 'BC-M12: Advanced Structural Design and Analysis',
    'module_hours': '240 hours',
    'number_of_classes': '3 (L6BC-A, L6BC-B, L6BC-C)',
    'date': '15/01/2025',
    'class_name': 'L6BC-A, L6BC-B, L6BC-C',
    
    # TERM 1
    'term1_weeks': '1-10',
    'term1_competence': 'BC-C12.1: Structural Analysis Fundamentals',
    'term1_learning_outcomes': '''Analyze structural loads and forces
Calculate bending moments and shear forces
Design structural members for different load conditions
Apply structural analysis software tools''',
    'term1_duration': '80 hours',
    'term1_indicative_contents': '''Types of loads (dead, live, wind, seismic)
Structural analysis methods (equilibrium, virtual work)
Bending moment and shear force diagrams
Deflection calculations
Introduction to SAP2000 and ETABS software''',
    
    # TERM 2
    'term2_weeks': '11-20',
    'term2_competence': 'BC-C12.2: Reinforced Concrete Design',
    'term2_learning_outcomes': '''Design reinforced concrete beams and columns
Calculate reinforcement requirements
Design concrete slabs and foundations
Apply building codes and standards''',
    'term2_duration': '80 hours',
    'term2_indicative_contents': '''Concrete properties and behavior
Reinforcement design principles
Beam design (flexure, shear, deflection)
Column design (axial load, biaxial bending)
Slab design (one-way, two-way, flat slabs)
Foundation design (isolated, combined, raft)''',
    
    # TERM 3
    'term3_weeks': '21-30',
    'term3_competence': 'BC-C12.3: Steel Structure Design',
    'term3_learning_outcomes': '''Design steel beams and columns
Design steel connections (bolted and welded)
Analyze steel frames and trusses
Prepare structural drawings and specifications''',
    'term3_duration': '80 hours',
    'term3_indicative_contents': '''Steel properties and section properties
Tension and compression member design
Beam design (lateral-torsional buckling)
Column design (buckling, effective length)
Connection design (bolts, welds, plates)
Truss analysis and design
Steel detailing and shop drawings''',
    
    # Signatures
    'prepared_by_name': 'NIYONZIMA Patrick',
    'prepared_by_position': 'Senior Trainer - Construction Department',
    'verified_by_name': 'UWIMANA Grace',
    'verified_by_position': 'Director of Studies',
    'approved_by_name': 'HABIMANA Emmanuel',
    'approved_by_position': 'School Manager'
}

try:
    scheme_file = fill_scheme_official(scheme_data)
    final_scheme = os.path.join(os.path.dirname(__file__), 'PROOFING_Scheme_of_Work.docx')
    
    import shutil
    shutil.copy(scheme_file, final_scheme)
    
    size = os.path.getsize(final_scheme)
    print(f"   SUCCESS: Scheme of Work generated: {size:,} bytes")
    print(f"   Location: {final_scheme}")
except Exception as e:
    print(f"   ERROR: {e}")
    import traceback
    traceback.print_exc()

print()
print("=" * 80)
print("PROOF-READING DOCUMENTS GENERATED SUCCESSFULLY")
print("=" * 80)
print()
print("Please review both documents for:")
print("   [OK] Proper formatting and spacing (1.5 line spacing)")
print("   [OK] Bold labels and normal content")
print("   [OK] School header with logo and location")
print("   [OK] All content properly aligned")
print("   [OK] No extra spacing or scattered text")
print("   [OK] Professional RTB-compliant appearance")
print()
print("Files location: backend/PROOFING_*.docx")
print("=" * 80)
