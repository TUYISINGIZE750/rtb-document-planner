// Offline DOCX Generator - Fallback when backend is unavailable
console.log('📄 Offline DOCX generator loaded');

// Simple DOCX generation using client-side libraries
function generateOfflineSessionPlan(formData) {
    const data = Object.fromEntries(formData);
    
    // Create a simple HTML structure that can be saved as DOC
    const docContent = `
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>RTB Session Plan - ${data.topic_of_session}</title>
    <style>
        body { font-family: 'Times New Roman', serif; margin: 1in; }
        .header { text-align: center; margin-bottom: 20px; }
        .title { font-size: 18px; font-weight: bold; color: #003366; }
        table { width: 100%; border-collapse: collapse; margin: 10px 0; }
        td, th { border: 1px solid #000; padding: 8px; vertical-align: top; }
        .label { font-weight: bold; background-color: #f0f0f0; }
        .section-header { background-color: #003366; color: white; font-weight: bold; text-align: center; }
    </style>
</head>
<body>
    <div class="header">
        <div class="title">RWANDA TECHNICAL BOARD</div>
        <div class="title">SESSION PLAN</div>
    </div>
    
    <table>
        <tr>
            <td class="label">Sector:</td>
            <td>${data.sector || ''}</td>
            <td class="label">Date:</td>
            <td>${data.date || ''}</td>
        </tr>
        <tr>
            <td class="label">Trainer:</td>
            <td colspan="2">${data.trainer_name || ''}</td>
            <td class="label">Term:</td>
            <td>${data.term || ''}</td>
        </tr>
        <tr>
            <td class="label">Module:</td>
            <td colspan="2">${data.module_code_title || ''}</td>
            <td class="label">Week:</td>
            <td>${data.week || ''}</td>
        </tr>
        <tr>
            <td class="label">Class:</td>
            <td>${data.class_name || ''}</td>
            <td class="label">Trainees:</td>
            <td>${data.number_of_trainees || ''}</td>
        </tr>
    </table>
    
    <table>
        <tr>
            <td class="section-header" colspan="2">LEARNING CONTENT</td>
        </tr>
        <tr>
            <td class="label">Topic of Session:</td>
            <td>${data.topic_of_session || ''}</td>
        </tr>
        <tr>
            <td class="label">Learning Outcomes:</td>
            <td>${(data.learning_outcomes || '').replace(/\\n/g, '<br>')}</td>
        </tr>
        <tr>
            <td class="label">Indicative Contents:</td>
            <td>${(data.indicative_contents || '').replace(/\\n/g, '<br>')}</td>
        </tr>
        <tr>
            <td class="label">Duration:</td>
            <td>${data.duration || '40'} minutes</td>
        </tr>
        <tr>
            <td class="label">Facilitation Technique:</td>
            <td>${data.facilitation_techniques || ''}</td>
        </tr>
    </table>
    
    <table>
        <tr>
            <td class="section-header" colspan="3">SESSION ACTIVITIES</td>
        </tr>
        <tr>
            <td class="label">Phase</td>
            <td class="label">Activities</td>
            <td class="label">Duration</td>
        </tr>
        <tr>
            <td class="label">Introduction</td>
            <td>
                • Greets and makes roll calls<br>
                • Reviews previous session<br>
                • Announces topic: "${data.topic_of_session}"<br>
                • Explains session objectives
            </td>
            <td>5 minutes</td>
        </tr>
        <tr>
            <td class="label">Development</td>
            <td>
                • Explains ${data.topic_of_session}<br>
                • Demonstrates practical examples<br>
                • Uses ${data.facilitation_techniques} approach<br>
                • Provides guided practice<br>
                • Monitors learner progress
            </td>
            <td>25 minutes</td>
        </tr>
        <tr>
            <td class="label">Conclusion</td>
            <td>
                • Summarizes key points<br>
                • Assesses learner understanding<br>
                • Provides feedback<br>
                • Links to next session
            </td>
            <td>10 minutes</td>
        </tr>
    </table>
    
    <p><strong>Note:</strong> This is a basic session plan generated offline. For full RTB-compliant formatting, please ensure the backend is properly deployed.</p>
</body>
</html>`;

    // Create and download the file
    const blob = new Blob([docContent], { 
        type: 'application/msword;charset=utf-8' 
    });
    
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = `RTB_Session_Plan_${data.topic_of_session?.replace(/[^a-zA-Z0-9]/g, '_') || 'Document'}.doc`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);
    
    return true;
}

function generateOfflineScheme(formData) {
    const data = Object.fromEntries(formData);
    
    const docContent = `
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>RTB Scheme of Work - ${data.module_code_title}</title>
    <style>
        body { font-family: 'Times New Roman', serif; margin: 0.5in; }
        .header { text-align: center; margin-bottom: 20px; }
        .title { font-size: 16px; font-weight: bold; }
        table { width: 100%; border-collapse: collapse; margin: 10px 0; font-size: 12px; }
        td, th { border: 1px solid #000; padding: 6px; vertical-align: top; }
        .label { font-weight: bold; background-color: #f0f0f0; }
        .header-cell { background-color: #d0d0d0; font-weight: bold; text-align: center; }
    </style>
</head>
<body>
    <div class="header">
        <div>${data.school || 'SCHOOL NAME'}</div>
        <div class="title">SCHEME OF WORK</div>
    </div>
    
    <table>
        <tr>
            <td class="label">Sector:</td>
            <td>${data.sector || ''}</td>
            <td class="label">Trainer:</td>
            <td>${data.trainer_name || ''}</td>
        </tr>
        <tr>
            <td class="label">Trade:</td>
            <td>${data.trade || ''}</td>
            <td class="label">School Year:</td>
            <td>${data.school_year || ''}</td>
        </tr>
        <tr>
            <td class="label">Module:</td>
            <td colspan="3">${data.module_code_title || ''}</td>
        </tr>
        <tr>
            <td class="label">RQF Level:</td>
            <td>${data.rqf_level || ''}</td>
            <td class="label">Module Hours:</td>
            <td>${data.module_hours || ''}</td>
        </tr>
    </table>
    
    <h3>Term 1</h3>
    <table>
        <tr>
            <th class="header-cell">Weeks</th>
            <th class="header-cell">Learning Outcomes</th>
            <th class="header-cell">Duration</th>
            <th class="header-cell">Indicative Content</th>
        </tr>
        <tr>
            <td>${data.term1_weeks || ''}</td>
            <td>${(data.term1_learning_outcomes || '').replace(/\\n/g, '<br>')}</td>
            <td>${data.term1_duration || ''}</td>
            <td>${(data.term1_indicative_contents || '').replace(/\\n/g, '<br>')}</td>
        </tr>
    </table>
    
    <h3>Term 2</h3>
    <table>
        <tr>
            <th class="header-cell">Weeks</th>
            <th class="header-cell">Learning Outcomes</th>
            <th class="header-cell">Duration</th>
            <th class="header-cell">Indicative Content</th>
        </tr>
        <tr>
            <td>${data.term2_weeks || ''}</td>
            <td>${(data.term2_learning_outcomes || '').replace(/\\n/g, '<br>')}</td>
            <td>${data.term2_duration || ''}</td>
            <td>${(data.term2_indicative_contents || '').replace(/\\n/g, '<br>')}</td>
        </tr>
    </table>
    
    <h3>Term 3</h3>
    <table>
        <tr>
            <th class="header-cell">Weeks</th>
            <th class="header-cell">Learning Outcomes</th>
            <th class="header-cell">Duration</th>
            <th class="header-cell">Indicative Content</th>
        </tr>
        <tr>
            <td>${data.term3_weeks || ''}</td>
            <td>${(data.term3_learning_outcomes || '').replace(/\\n/g, '<br>')}</td>
            <td>${data.term3_duration || ''}</td>
            <td>${(data.term3_indicative_contents || '').replace(/\\n/g, '<br>')}</td>
        </tr>
    </table>
    
    <p><strong>Prepared by:</strong> ${data.trainer_name || ''}</p>
    <p><strong>DOS:</strong> ${data.dos_name || ''}</p>
    <p><strong>Manager:</strong> ${data.manager_name || ''}</p>
    
    <p><strong>Note:</strong> This is a basic scheme generated offline. For full RTB-compliant formatting, please ensure the backend is properly deployed.</p>
</body>
</html>`;

    const blob = new Blob([docContent], { 
        type: 'application/msword;charset=utf-8' 
    });
    
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = `RTB_Scheme_of_Work_${data.module_code_title?.replace(/[^a-zA-Z0-9]/g, '_') || 'Document'}.doc`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);
    
    return true;
}