import json,re
d=json.load(open('metax/metax.json')); zh=json.load(open('metax/zh.json'))
rows={r[0]:r for r in json.load(open('metax/_mapping_scan.json'))}
idx={e['title']:e for e in json.load(open('wiki/index.json'))}
P=lambda t: idx[t]['path']
# --- 挂载现有（含人工复核的模糊匹配）；值为条目 title
MOUNT={
 'feedback':'Feedback','feedback_(comments_vs._grades)':'Feedback','feedback_(corrective,_reinforcement_&_cues)':'Feedback',
 'feedback_(from_student_re_quality)':'Feedback','feedback_(from_tests)':'Feedback','feedback_(self)':'Feedback',
 'feedback_(tasks_&_processes)':'Feedback','feedback_(technology)':'Feedback','feedback_(timing)':'Feedback',
 'blended_learning':'Blended Learning','classroom_management':'Classroom Management','cognitive_task_analysis':'Cognitive Task Analysis',
 'concept_mapping':'Concept Mapping','constructivist_teaching':'Constructivist Instruction','cooperative_learning':'Cooperative Learning',
 'critical_thinking':'Critical Thinking','direct_instruction':'Direct Instruction','executive_functioning':'Executive Function',
 'flow':'Flow','formative_evaluation':'Formative Assessment','homework':'Homework','individual_instruction':'Individualised Instruction',
 'inquiry-based_teaching':'Inquiry-Based Learning','intelligent_tutoring_systems':'Intelligent Tutoring Systems','jigsaw_method':'Jigsaw',
 'locus_of_control':'Locus of Control','outcomes_based_education':'Outcomes-based Education','peer_tutoring':'Peer-Supported Learning',
 'peer_tutoring_on_tutee':'Peer-Supported Learning','peer_tutoring_on_tutor':'Peer-Supported Learning',
 'problem-based_learning':'Problem-Based Learning','productive_failure_(errors)':'Productive Failure','project-based_learning':'Project-Based Learning',
 'reading_recovery':'Reading Recovery','response_to_intervention':'Response to Intervention','retention':'Grade Retention',
 'school_choice':'School Choice','self-directed_learning':'Self-Directed Learning','self-efficacy':'Self-Efficacy','teacher_self-efficacy':'Self-Efficacy',
 'self_control':'Self-control','socio-emotional_learning':'Social-Emotional Learning','socioeconomic_status':'Socioeconomic Status',
 'peer_socioeconomic_status':'Socioeconomic Status','stereotype_threat':'Stereotype Threat','success_criteria':'Success Criteria',
 'teacher-student_relationships':'Student-Teacher Relationship','teacher_clarity':'Teacher Clarity','time-on-task':'Time on Task',
 'mobility':'Student Mobility','help_seeking':'Academic Help-Seeking','seeking_help_from_peers':'Academic Help-Seeking',
 'immediacy':'Teacher Immediacy','growth_vs._fixed_mindsets':'Growth Mindset','initial_teacher_education_programs':'Initial Teacher Training',
 'micro-teaching~video_review_of_lessons':'Microteaching','reducing_class_size':'Class Size','robotics':'Educational Robotics',
 'positive_self-concept':'Academic Self-Concept','self-regulation_strategies':'Self-Regulated Learning','creativity_programs':'Creativity Training',
 'open_vs._traditional_classrooms':'Open Classroom Movement','meta-cognition_strategies':'Metacognition','epistemic_cognitive_training':'Epistemic Cognition',
 'principals~school_leaders':'School Leadership','stem_programs':'STEM Education','whole_language_approach':'Whole Language',
 'working_memory_strength':'Working Memory','working_memory_training':'Working Memory','teacher_performance_pay':'Performance Pay',
 'correlating_learning_styles_to_achievement':'Learning Styles','matching_teaching_to_style_of_learning':'Learning Styles',
 'ability_grouping_for_gifted_students':'Tracking','tracking~streaming':'Tracking','detracking':'Tracking',
 'student-centered_teaching':'Learner-Centred Education','discovery-based_teaching':'Discovery Learning',
 'scaffolding_and_situated_learning':'Scaffolding','school_effects':'School Effectiveness','chatgpt':'Generative Artificial Intelligence',
 'chatbot':'Conversational AI in Education','private_tutoring':'Cram Schools','gender_(male-female)':'Gender Differences in Academic Achievement',
 'gender_(male-female)_on_creativity':'Gender Differences in Academic Achievement','gender_(male-female)_on_math':'Gender Differences in Academic Achievement',
 'gender_(male-female)_on_reading':'Gender Differences in Academic Achievement','gender_(male-female)_on_science':'Gender Differences in Academic Achievement',
 'simulations':'Computer Simulation','learning_strategies':None,
}
# --- 待确认的挂载（语义接近但不完全一致）
TENTATIVE={'artificial_intelligence':'Generative Artificial Intelligence','gaming':'Gamification','concentration-persistence-engagement':'Student Engagement',
 'within-class_grouping':'Tracking','coding':'Computational Thinking','argumentation~classroom_discussion':'Dialogue in Education',
 'teacher_collaboration':'Professional Learning Community','mathematics_problem_solving':'Problem Solving','problem-solving_teaching':'Problem Solving',
 'mentoring':'Mentorship'}
# --- 新建条目合并成族（族标题: [ids]）
FAMILY={
 'Academic Emotions':['emotions','enjoyment','boredom','anger','frustration','relaxation','happiness','hope','humor'],
 'Academic Anxiety':['anxiety','anxiety_on_math~science','test_anxiety','anxiety_reducing_programs'],
 'Game-Based Learning':['gaming','gaming_in_esl','gaming_in_language','gaming_in_math','gaming_in_science','video_games'],
 'Student Personality Traits':['student_personality','student_personality:_agreeableness','student_personality:_consientiousness','student_personality:_extraversion','student_personality:_neuroticism','student_personality:_open_to_experience'],
 'Technology in Subject Teaching':['technology_in_language','technology_in_mathematics','technology_in_other_subjects','technology_in_reading~literacy','technology_in_science','technology_in_writing'],
 'Educational Technology Across Learner Groups':['technology_in_small_groups','technology_with_college_students','technology_with_elementary_students','technology_with_high_school_students','technology_with_learning_needs_students'],
 'Virtual Reality in Education':['virtual_reality','virtual_reality_in_languages','virtual_reality_in_science~math'],
 'Mathematics Intervention Programs':['mathematics_curricula_&_programs','mathematics_direct_or_guided','mathematics_programs_-_other','mathematics_programs_for_ld','mathematics_teaching_specific_skills','manipulative_materials_on_math'],
 'Teacher Professional Development Programs':['professional_development_programs','professional_development_re_early_childhood','professional_development_re_literacy','professional_development_re_math~science'],
 'Achievement Goal Orientations':['mastery_goals_-_approach','mastery_goals_-_avoidance','performance_goals_-_approach','performance_goals_-_avoidance'],
 'Student Approaches to Learning':['achieving_motivation_and_approach','deep_motivation_and_approach','surface_motivation_and_approach'],
 'Parental Involvement in Education':['parental_involvement','parental_involvement_with_homework','parental_expectations','parental_programs','parental_literacy_programs','parent~adult_tutoring'],
 'Parenting Styles and Support':['parental_authoritarian_support','parental_autonomy_support','corporal_punishment_in_the_home'],
 'Student Motivation':['motivation','motivation_programs','perceived_task_value'],
 'Tutoring Interventions':['tutoring','one-on-one_tutoring','tutoring~multimedia'],
 'Mindfulness Interventions in Schools':['mindfulness','mindfulness_interventions','meditation_interventions'],
 'Cooperative, Competitive and Individualistic Learning':['competitive_vs._individualistic_learning','cooperative_vs._competitive_learning','cooperative_vs._individualistic_learning','competitive_climate'],
 'Preschool Education Programs':['pre-school_programs','pre-school_with_at-risk_students','pre_school_to_later_learning','early_intervention_types','head_start_programs'],
 'Teacher Expectations':['teacher_expectations','teacher_expectations_-_physical_attractiveness','teacher_estimates_of_achievement_','teachers_labeling_students'],
 'Whole-School Improvement':['whole-school_improvement_programs','whole-school_reduction_of_achievement_gap','school-wide'],
 'Practice Testing and Retrieval':['practice_testing','retrieval_practice','frequent_testing','effects_of_testing'],
 'Reading Programs':['comprehensive_reading_programs','comprehensive_reading_programs_for_hs','reading_comprehension_programs','reading_programs_for_specific_groups','repeated_reading_programs','conjoint_reading_programs','music-based_reading_programs'],
 'Family Structure and Achievement':['family_structure','non-_vs_divorced_families','remarriage','engaged_vs._disengaged_fathers','non-adopted_vs._adopted_children','mother_employment','children_into_care_homes'],
}
# --- 单项新建：标题与中文别名覆写（短名、泛名、含 / ( ) vs 的名称）
TITLE={
 'clickers':('Classroom Response Systems','课堂应答系统'),'smartboards':('Interactive Whiteboards','交互式白板'),'moocs':('Massive Open Online Courses','慕课'),
 'webinars':('Webinar-Based Learning','网络研讨会学习'),'self_monitoring':('Self-Monitoring in Learning','学习自我监控'),'learning_strategies':('Learning Strategies','学习策略'),
 'desegregation':('School Desegregation','学校种族融合'),'breastfeeding':('Breastfeeding and Cognitive Development','母乳喂养与认知发展'),
 'perfectionism':('Perfectionism','完美主义'),'cross-laterality':('Cross-Laterality Training','交叉侧性训练'),
 'questioning':('Teacher Questioning','课堂提问'),'lectures':('Lecturing','讲授法'),'fitness':('Physical Fitness and Achievement','体质健康'),
 'curiosity':('Epistemic Curiosity','学习好奇心'),'illness':('Childhood Illness and Achievement','儿童疾病'),'belonging':('Sense of School Belonging','学校归属感'),
 'home_visiting':('Home Visiting Programs','家访项目'),'charter_schools':('Charter Schools','特许学校'),'vouchers':('School Vouchers','教育券'),
 'procrastination':('Academic Procrastination','学业拖延'),'friendship':('Peer Friendship','同伴友谊'),'teacher_qualifications':('Teacher Qualifications','教师资质'),
 'rubrics':('Scoring Rubrics','评分量规'),'differentiation':('Differentiated Instruction','差异化教学'),'school_size':('School Size Effects','学校规模效应'),
 'self_assessment':('Student Self-Assessment','学生自我评价'),'collaborative_learning':('Collaborative Learning','协作学习'),'extracurricular_activities':('Extracurricular Activities','课外活动'),
 'depression':('Student Depression','学生抑郁'),'covid':('COVID-19 Disruption to Schooling','新冠疫情停课'),'bullying':('School Bullying','校园欺凌'),
 'grant_aid':('Student Grant Aid','学生助学金'),'systems~accountability_systems':('School Accountability Systems','学校问责制度'),'teacher-student_support':('Teacher Support for Students','教师支持'),
 'attendance_(lack_of)':('Student Absenteeism','学生缺勤'),'coaching':('Instructional Coaching','教学教练指导'),'design_thinking':('Design Thinking in Education','设计思维教育'),
 'personalized_learning':('Personalized Learning','个性化学习'),'web-based_learning':('Web-Based Learning','网络学习'),'peer_assessment':('Peer Assessment','同伴互评'),
 're-reading':('Rereading','重读策略'),'well-being':('Student Well-being','学生幸福感'),'deliberate_practice':('Deliberate Practice','刻意练习'),'time_management':('Time Management','时间管理'),
 'aggression~violence':('Student Aggression and Violence','学生攻击与暴力'),'audio~visual_methods':('Audiovisual Instruction','视听教学'),'co-~team_teaching':('Co-Teaching','协同教学'),
 'ipads~touch_devices':('Tablets and Touch Devices in Learning','平板与触屏学习'),'outdoor~adventure_programs':('Outdoor Adventure Education','户外探险教育'),
 'character~positive_programs':('Character and Positive Education Programs','品格与积极教育项目'),'consolidating~turnaround~merging_schools':('School Consolidation and Turnaround','学校合并与转型'),
 'suspension~expelling_students':('Student Suspension and Expulsion','停学与开除'),'multi-grade~age_classes':('Multi-Grade Classes','复式班级'),
 'mainstreaming~inclusion':('Inclusive Education','融合教育'),'modifying_school_calendars~timetables':('School Calendar Modification','校历调整'),
 'interactive_video~multimedia':('Interactive Video and Multimedia','交互视频与多媒体'),'spatial_skills~training':('Spatial Skills Training','空间能力训练'),
 'self-verbalization~self_questioning':('Self-Verbalization and Self-Questioning','自我言语化与自我提问'),'pre-term~low_birth_weight_vs._full_term':('Preterm Birth and Low Birth Weight','早产与低出生体重'),
 'spaced_vs._mass_practice':('Spaced Practice','分散练习'),'in_vs_out_of_field_teaching':('Out-of-Field Teaching','非专业对口教学'),'morning_vs._evening':('Chronotype and Achievement','晨型与夜型'),
 'print_vs._digital':('Print Versus Digital Reading','纸质与数字阅读'),'family_on_welfare~state_aid':('Family Welfare Receipt','家庭领取社会救助'),
 'lack_of_sleep':('Sleep Deprivation in Students','学生睡眠不足'),'sugar':('Sugar Intake and Learning','糖摄入与学习'),'finances':('School Finances','学校经费'),
 'imagery':('Mental Imagery Strategies','心理表象策略'),'emotional_intelligence':('Emotional Intelligence','情绪智力'),'grit':('Grit','坚毅'),
 'artificial_intelligence':('Artificial Intelligence in Education','教育人工智能'),'covid':('COVID-19 Disruption to Schooling','新冠疫情停课'),
 'student_control_over_learning':('Student Control over Learning','学生学习控制权'),'adverse_child_events':('Adverse Childhood Experiences','童年不良经历'),
 'background_music':('Background Music While Studying','学习背景音乐'),'summarizing':('Summarization Strategies','概括策略'),'mnemonics':('Mnemonic Strategies','记忆术'),
 'note-taking':('Note-Taking','记笔记'),'humor':('Humor in Teaching','教学幽默'),'pets_in_class':('Classroom Pets','班级宠物'),'autism':('Autism Spectrum Disorder','孤独症谱系障碍'),
}
GENERIC_ZH={'动机','焦虑','希望','情绪','辅导','讲授','提问','体能','疾病','乐趣','愤怒','放松','友谊','幸福感','幽默','模拟','编程','游戏化学习','求助','拖延'}
def default_title(name):
    t=re.sub(r'\s*/\s*',' and ',name); t=re.sub(r'\s*\(.*?\)\s*',' ',t).strip()
    t=re.sub(r'\bvs\.?\b','Versus',t)
    small={'and','of','in','on','to','for','with','the','a','versus','vs'}
    return ' '.join(w if (i and w.lower() in small) else (w[:1].upper()+w[1:]) for i,w in enumerate(t.split()))
fam_of={i:f for f,ids in FAMILY.items() for i in ids}
out=[]
for iid,inf in d['influences'].items():
    r=rows[iid]; z=zh['influences'][iid]; risk=max(r[4],r[5])
    if iid in MOUNT and MOUNT[iid]:
        act,target,alias='挂载',MOUNT[iid],''
    elif iid in TENTATIVE:
        act,target,alias='挂载？',TENTATIVE[iid],''
    elif iid in fam_of:
        act,target,alias='新建（合并）',fam_of[iid],''
    else:
        t,a=TITLE.get(iid,(default_title(inf['name']),z))
        act,target,alias='新建',t,a
    flag=''
    if act.startswith('新建') and iid not in TITLE and iid not in fam_of and (len(inf['name'].split())==1 or risk>=15 or z in GENERIC_ZH): flag='名称需复核'
    out.append(dict(id=iid,name=inf['name'],zh=z,domain=zh['domain'][inf['domain']],sub=zh['sub_domain'][inf['sub_domain']],action=act,target=target,alias=alias,risk=risk,flag=flag))
json.dump(out,open('metax/mapping.json','w'),ensure_ascii=False,indent=1)
import collections
c=collections.Counter(o['action'] for o in out); print(c)
newtitles={o['target'] for o in out if o['action'].startswith('新建')}
print('new entries',len(newtitles),'mount targets',len({o['target'] for o in out if o['action']=='挂载'}))
print('needs review',sum(1 for o in out if o['flag']))
dups=[t for t in newtitles if t in idx]; print('new titles that already exist:',dups)
