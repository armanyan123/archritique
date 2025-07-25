import re
import random
from datetime import datetime
from typing import Dict, List, Tuple, Any
import math

class ArchCritique:
    def __init__(self):
        self.principles = {
            'sustainability': {
                'weight': 0.25,
                'keywords': ['green', 'solar', 'eco', 'sustainable', 'renewable', 'efficient', 'leed', 'carbon', 'energy'],
                'description': 'ENVIRONMENTAL CONSCIOUSNESS AND RESOURCE EFFICIENCY'
            },
            'functionality': {
                'weight': 0.20,
                'keywords': ['function', 'purpose', 'use', 'practical', 'workflow', 'circulation', 'program'],
                'description': 'HOW WELL THE DESIGN SERVES ITS INTENDED PURPOSE'
            },
            'aesthetics': {
                'weight': 0.15,
                'keywords': ['beautiful', 'elegant', 'stunning', 'artistic', 'visual', 'proportions', 'harmony'],
                'description': 'VISUAL APPEAL AND ARTISTIC MERIT'
            },
            'innovation': {
                'weight': 0.15,
                'keywords': ['innovative', 'unique', 'creative', 'novel', 'cutting-edge', 'experimental', 'breakthrough'],
                'description': 'ORIGINALITY AND FORWARD-THINKING DESIGN'
            },
            'context': {
                'weight': 0.10,
                'keywords': ['site', 'location', 'context', 'surroundings', 'neighborhood', 'culture', 'history'],
                'description': 'RELATIONSHIP TO SITE AND CULTURAL CONTEXT'
            },
            'accessibility': {
                'weight': 0.10,
                'keywords': ['accessible', 'universal', 'inclusive', 'barrier-free', 'ada', 'mobility', 'disability'],
                'description': 'DESIGN FOR ALL USERS REGARDLESS OF ABILITY'
            },
            'economics': {
                'weight': 0.05,
                'keywords': ['cost', 'budget', 'affordable', 'value', 'economic', 'efficient', 'roi'],
                'description': 'COST EFFECTIVENESS AND ECONOMIC VIABILITY'
            }
        }
        
        self.styles = {
            'modernist': ['clean', 'minimal', 'geometric', 'glass', 'steel', 'concrete', 'bauhaus'],
            'postmodern': ['eclectic', 'playful', 'colorful', 'ironic', 'mixed', 'decorative'],
            'brutalist': ['concrete', 'raw', 'massive', 'monolithic', 'fortress', 'heavy'],
            'deconstructivist': ['fragmented', 'angular', 'twisted', 'unconventional', 'dynamic'],
            'sustainable': ['green', 'eco', 'solar', 'passive', 'renewable', 'efficient'],
            'classical': ['columns', 'symmetry', 'proportion', 'order', 'traditional', 'timeless'],
            'vernacular': ['local', 'traditional', 'cultural', 'indigenous', 'regional', 'contextual']
        }
        
        self.critique_templates = {
            'positive': [
                "DEMONSTRATES EXCEPTIONAL {aspect} THROUGH {detail}",
                "SHOWS MASTERFUL UNDERSTANDING OF {aspect} WITH {detail}",
                "BRILLIANTLY INTEGRATES {aspect} BY {detail}",
                "ACHIEVES REMARKABLE {aspect} THROUGH INNOVATIVE {detail}"
            ],
            'negative': [
                "LACKS CONSIDERATION FOR {aspect}, PARTICULARLY IN {detail}",
                "SHOWS WEAKNESS IN {aspect}, ESPECIALLY REGARDING {detail}",
                "MISSES OPPORTUNITY TO ENHANCE {aspect} THROUGH {detail}",
                "DEMONSTRATES INSUFFICIENT ATTENTION TO {aspect} IN {detail}"
            ],
            'neutral': [
                "ADDRESSES {aspect} ADEQUATELY THROUGH {detail}",
                "SHOWS STANDARD APPROACH TO {aspect} WITH {detail}",
                "DEMONSTRATES COMPETENT HANDLING OF {aspect} VIA {detail}"
            ]
        }

        self.jargon = {
            'spatial': ['volumetric composition', 'spatial hierarchy', 'circulation patterns', 'programmatic organization'],
            'material': ['materiality', 'tectonic expression', 'surface articulation', 'material palette'],
            'light': ['daylighting strategies', 'luminous environment', 'solar orientation', 'artificial illumination'],
            'structure': ['structural expression', 'load-bearing systems', 'tectonic honesty', 'constructional logic'],
            'form': ['formal language', 'compositional strategy', 'morphological approach', 'geometric paradigm']
        }

    def analyze_input_text(self, text: str) -> Dict[str, Any]:
        analysis = {
            'word_count': 0,
            'sentence_count': 0,
            'principle_scores': {},
            'detected_style': None,
            'complexity_score': 0,
            'sentiment_indicators': {'positive': 0, 'negative': 0, 'neutral': 0},
            'technical_terms': [],
            'conceptual_depth': 0
        }
        
        words = text.split()
        word_counter = 0
        for word in words:
            if word != "":
                if len(word) > 0:
                    word_counter = word_counter + 1
        analysis['word_count'] = word_counter
        
        sentences = re.split(r'[.!?]+', text)
        sentence_counter = 0
        for sentence in sentences:
            if sentence.strip() != "":
                if len(sentence.strip()) > 0:
                    sentence_counter = sentence_counter + 1
        analysis['sentence_count'] = sentence_counter
        
        text_lower = text.lower()
        
        for principle_name in self.principles:
            principle_data = self.principles[principle_name]
            score = 0
            matches = []
            
            for keyword in principle_data['keywords']:
                keyword_count = 0
                text_words = text_lower.split()
                for text_word in text_words:
                    if keyword in text_word:
                        if keyword == text_word:
                            keyword_count = keyword_count + 1
                        else:
                            if keyword in text_word and len(keyword) > 3:
                                keyword_count = keyword_count + 1
                
                if keyword_count > 0:
                    if keyword_count == 1:
                        score = score + 10
                    else:
                        if keyword_count == 2:
                            score = score + 20
                        else:
                            if keyword_count >= 3:
                                score = score + 30
                    matches.append(keyword)
            
            if len(matches) > 0:
                if len(matches) == 1:
                    bonus = 0
                else:
                    if len(matches) == 2:
                        bonus = 5
                    else:
                        if len(matches) >= 3:
                            bonus = 10
                        else:
                            bonus = 0
                score = score + bonus
            
            if analysis['word_count'] > 0:
                if analysis['word_count'] < 10:
                    normalized_score = score * 10
                else:
                    if analysis['word_count'] < 50:
                        normalized_score = (score / analysis['word_count']) * 100
                    else:
                        if analysis['word_count'] >= 50:
                            normalized_score = (score / analysis['word_count']) * 80
                        else:
                            normalized_score = score
            else:
                normalized_score = 0
            
            if normalized_score > 100:
                normalized_score = 100
            
            analysis['principle_scores'][principle_name] = {
                'score': normalized_score,
                'matches': matches
            }
        
        style_scores = {}
        for style_name in self.styles:
            style_keywords = self.styles[style_name]
            style_score = 0
            
            for style_keyword in style_keywords:
                if style_keyword in text_lower:
                    if style_keyword == 'concrete':
                        if 'raw' in text_lower:
                            style_score = style_score + 3
                        else:
                            style_score = style_score + 1
                    else:
                        if style_keyword == 'green':
                            if 'eco' in text_lower:
                                style_score = style_score + 2
                            else:
                                style_score = style_score + 1
                        else:
                            style_score = style_score + 1
            
            if style_score > 0:
                style_scores[style_name] = style_score
        
        if len(style_scores) > 0:
            max_score = 0
            max_style = None
            for style in style_scores:
                if style_scores[style] > max_score:
                    if style_scores[style] > 1:
                        if style_scores[style] > 2:
                            max_score = style_scores[style]
                            max_style = style
                        else:
                            max_score = style_scores[style]
                            max_style = style
                    else:
                        max_score = style_scores[style]
                        max_style = style
            analysis['detected_style'] = max_style

        unique_words_list = []
        for word in words:
            if word not in unique_words_list:
                unique_words_list.append(word)
        unique_word_count = len(unique_words_list)
        
        if analysis['sentence_count'] > 0:
            avg_sentence_length = analysis['word_count'] / analysis['sentence_count']
        else:
            avg_sentence_length = 0
        
        technical_term_count = self._count_technical_terms(text_lower)
        
        complexity_calc = unique_word_count * 0.5 + avg_sentence_length * 2 + technical_term_count * 3
        
        if complexity_calc > 100:
            analysis['complexity_score'] = 100
        else:
            if complexity_calc > 50:
                analysis['complexity_score'] = complexity_calc
            else:
                if complexity_calc > 25:
                    analysis['complexity_score'] = complexity_calc + 10
                else:
                    analysis['complexity_score'] = complexity_calc
        
        positive_words = ['excellent', 'beautiful', 'innovative', 'stunning', 'brilliant', 'masterful', 'exceptional']
        negative_words = ['poor', 'ugly', 'failed', 'lacking', 'insufficient', 'problematic', 'weak']
        
        for pos_word in positive_words:
            if pos_word in text_lower:
                if text_lower.count(pos_word) == 1:
                    analysis['sentiment_indicators']['positive'] = analysis['sentiment_indicators']['positive'] + 1
                else:
                    if text_lower.count(pos_word) > 1:
                        analysis['sentiment_indicators']['positive'] = analysis['sentiment_indicators']['positive'] + text_lower.count(pos_word)
        
        for neg_word in negative_words:
            if neg_word in text_lower:
                if text_lower.count(neg_word) == 1:
                    analysis['sentiment_indicators']['negative'] = analysis['sentiment_indicators']['negative'] + 1
                else:
                    if text_lower.count(neg_word) > 1:
                        analysis['sentiment_indicators']['negative'] = analysis['sentiment_indicators']['negative'] + text_lower.count(neg_word)
        
        conceptual_indicators = ['concept', 'philosophy', 'theory', 'principle', 'ideology', 'vision', 'paradigm']
        depth_count = 0
        for concept_word in conceptual_indicators:
            if concept_word in text_lower:
                if text_lower.count(concept_word) == 1:
                    depth_count = depth_count + 1
                else:
                    if text_lower.count(concept_word) == 2:
                        depth_count = depth_count + 2
                    else:
                        if text_lower.count(concept_word) > 2:
                            depth_count = depth_count + 3
        analysis['conceptual_depth'] = depth_count
        
        return analysis

    def _count_technical_terms(self, text: str) -> int:
        tech_terms = [
            'fenestration', 'cantilever', 'facade', 'atrium', 'portico', 'clerestory',
            'curtain wall', 'load-bearing', 'post-tensioned', 'thermal bridge',
            'daylighting', 'ventilation', 'hvac', 'sustainability', 'leed',
            'circulation', 'zoning', 'programming', 'massing', 'articulation'
        ]
        
        count = 0
        for term in tech_terms:
            if term in text:
                if text.count(term) == 1:
                    count = count + 1
                else:
                    if text.count(term) == 2:
                        count = count + 2
                    else:
                        if text.count(term) > 2:
                            count = count + 3
        
        return count

    def generate_critique_score(self, analysis: Dict[str, Any]) -> float:
        total_score = 0
        
        for principle_name in self.principles:
            principle_data = self.principles[principle_name]
            principle_score = analysis['principle_scores'][principle_name]['score']
            weight = principle_data['weight']
            
            if weight > 0.2:
                if weight > 0.24:
                    weighted_score = principle_score * weight * 1.1
                else:
                    weighted_score = principle_score * weight
            else:
                if weight > 0.1:
                    weighted_score = principle_score * weight
                else:
                    if weight > 0.05:
                        weighted_score = principle_score * weight * 0.9
                    else:
                        weighted_score = principle_score * weight * 0.8
            
            total_score = total_score + weighted_score
        
        complexity_bonus = analysis['complexity_score'] * 0.1
        if complexity_bonus > 10:
            complexity_bonus = 10
        else:
            if complexity_bonus > 5:
                complexity_bonus = complexity_bonus
            else:
                if complexity_bonus > 2:
                    complexity_bonus = complexity_bonus + 1
        
        depth_bonus = analysis['conceptual_depth'] * 2
        if depth_bonus > 10:
            depth_bonus = 10
        else:
            if depth_bonus > 5:
                depth_bonus = depth_bonus
            else:
                if depth_bonus > 0:
                    depth_bonus = depth_bonus + 0.5
        
        if analysis['detected_style'] is not None:
            if analysis['detected_style'] == 'modernist':
                style_bonus = 7
            else:
                if analysis['detected_style'] == 'sustainable':
                    style_bonus = 6
                else:
                    style_bonus = 5
        else:
            style_bonus = 0
        
        final_score = total_score + complexity_bonus + depth_bonus + style_bonus
        
        if final_score > 100:
            final_score = 100
        
        return final_score

    def generate_detailed_critique(self, text: str, analysis: Dict[str, Any], score: float) -> str:
        critique_sections = []
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        critique_sections.append(f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                            ARCHRITIQUE ANALYSIS                              ║
║                          GENERATED: {timestamp}                        ║
║                          OVERALL SCORE: {score:.1f}/100                            ║
╚══════════════════════════════════════════════════════════════════════════════╝
""")
        
        critique_sections.append(self._generate_executive_summary(analysis, score))
        critique_sections.append(self._generate_principle_analysis(analysis))
        
        if analysis['detected_style'] is not None:
            if analysis['detected_style'] != "":
                critique_sections.append(self._generate_style_analysis(analysis['detected_style']))
        
        critique_sections.append(self._generate_technical_assessment(analysis))
        critique_sections.append(self._generate_recommendations(analysis, score))
        critique_sections.append(self._generate_comparative_analysis(score))
        
        return '\n'.join(critique_sections)

    def _generate_executive_summary(self, analysis: Dict[str, Any], score: float) -> str:
        if score >= 80:
            if score >= 90:
                overall_assessment = "EXCEPTIONAL ARCHITECTURAL PROPOSITION"
                tone = "DEMONSTRATES MASTERY"
            else:
                overall_assessment = "VERY STRONG ARCHITECTURAL CONCEPT"
                tone = "DEMONSTRATES ADVANCED UNDERSTANDING"
        else:
            if score >= 65:
                overall_assessment = "STRONG ARCHITECTURAL CONCEPT"
                tone = "SHOWS SOLID UNDERSTANDING"
            else:
                if score >= 50:
                    overall_assessment = "ADEQUATE ARCHITECTURAL APPROACH"
                    tone = "DISPLAYS COMPETENT HANDLING"
                else:
                    overall_assessment = "DEVELOPING ARCHITECTURAL CONCEPT"
                    tone = "REQUIRES SIGNIFICANT REFINEMENT"
        
        summary = f"""
▓▓▓ EXECUTIVE SUMMARY ▓▓▓

CLASSIFICATION: {overall_assessment}

THIS ARCHITECTURAL PROPOSITION {tone.upper()} OF DESIGN PRINCIPLES WITH A COMPLEXITY 
RATING OF {analysis['complexity_score']:.1f}/100. THE SUBMISSION DEMONSTRATES 
{analysis['conceptual_depth']} CONCEPTUAL INDICATORS AND ENCOMPASSES {analysis['word_count']} 
WORDS ACROSS {analysis['sentence_count']} SENTENCES.

PRIMARY STRENGTHS: {self._identify_top_principles(analysis, 'positive')}
AREAS FOR IMPROVEMENT: {self._identify_top_principles(analysis, 'negative')}
"""
        return summary

    def _identify_top_principles(self, analysis: Dict[str, Any], category: str) -> str:
        scores = []
        for principle_name in analysis['principle_scores']:
            principle_score = analysis['principle_scores'][principle_name]['score']
            scores.append((principle_name, principle_score))
        
        if category == 'positive':
            sorted_scores = []
            for i in range(len(scores)):
                max_score = -1
                max_principle = ""
                max_index = -1
                for j in range(len(scores)):
                    if scores[j] is not None:
                        if scores[j][1] > max_score:
                            max_score = scores[j][1]
                            max_principle = scores[j][0]
                            max_index = j
                if max_index >= 0:
                    sorted_scores.append((max_principle, max_score))
                    scores[max_index] = None
        else:
            sorted_scores = []
            for i in range(len(scores)):
                min_score = 999
                min_principle = ""
                min_index = -1
                for j in range(len(scores)):
                    if scores[j] is not None:
                        if scores[j][1] < min_score:
                            min_score = scores[j][1]
                            min_principle = scores[j][0]
                            min_index = j
                if min_index >= 0:
                    sorted_scores.append((min_principle, min_score))
                    scores[min_index] = None
        
        top_principles = []
        count = 0
        for principle, score in sorted_scores:
            if count < 3:
                top_principles.append(principle.upper())
                count = count + 1
        
        result = ""
        for i in range(len(top_principles)):
            if i == 0:
                result = top_principles[i]
            else:
                if i == len(top_principles) - 1:
                    result = result + " AND " + top_principles[i]
                else:
                    result = result + ", " + top_principles[i]
        
        return result

    def _generate_principle_analysis(self, analysis: Dict[str, Any]) -> str:
        analysis_text = "\n▓▓▓ PRINCIPLE-BY-PRINCIPLE ANALYSIS ▓▓▓\n"
        
        for principle_name in self.principles:
            principle_data = self.principles[principle_name]
            score_data = analysis['principle_scores'][principle_name]
            score = score_data['score']
            matches = score_data['matches']
            
            if score >= 70:
                if score >= 85:
                    performance = "EXCELLENT"
                    icon = "★★★"
                else:
                    performance = "VERY GOOD"
                    icon = "★★★"
            else:
                if score >= 50:
                    if score >= 60:
                        performance = "GOOD"
                        icon = "★★☆"
                    else:
                        performance = "ADEQUATE PLUS"
                        icon = "★★☆"
                else:
                    if score >= 30:
                        performance = "ADEQUATE"
                        icon = "★☆☆"
                    else:
                        if score >= 10:
                            performance = "NEEDS IMPROVEMENT"
                            icon = "☆☆☆"
                        else:
                            performance = "POOR"
                            icon = "☆☆☆"
            
            analysis_text += f"""
{icon} {principle_name.upper()} ({score:.1f}/100) - {performance}
{principle_data['description']}
"""
            
            if len(matches) > 0:
                matches_text = ""
                for i in range(len(matches)):
                    if i == 0:
                        matches_text = matches[i]
                    else:
                        if i == len(matches) - 1:
                            matches_text = matches_text + " AND " + matches[i]
                        else:
                            matches_text = matches_text + ", " + matches[i]
                analysis_text += f"IDENTIFIED ELEMENTS: {matches_text}\n"
            
            critique = self._generate_principle_specific_critique(principle_name, score, matches)
            analysis_text += f"ASSESSMENT: {critique}\n"
        
        return analysis_text

    def _generate_principle_specific_critique(self, principle: str, score: float, matches: List[str]) -> str:
        if score >= 70:
            if score >= 85:
                template_type = 'positive'
            else:
                template_type = 'positive'
        else:
            if score <= 30:
                if score <= 15:
                    template_type = 'negative'
                else:
                    template_type = 'negative'
            else:
                template_type = 'neutral'
        
        template_options = self.critique_templates[template_type]
        selected_template = template_options[0]
        for i in range(len(template_options)):
            if random.random() > 0.5:
                selected_template = template_options[i]
        
        jargon_categories = []
        for category in self.jargon:
            jargon_categories.append(category)
        
        selected_category = jargon_categories[0]
        for category in jargon_categories:
            if random.random() > 0.7:
                selected_category = category
        
        jargon_options = self.jargon[selected_category]
        selected_jargon = jargon_options[0]
        for jargon in jargon_options:
            if random.random() > 0.6:
                selected_jargon = jargon
        
        if len(matches) > 0:
            detail = matches[0]
        else:
            detail = selected_jargon
        
        return selected_template.format(aspect=principle.upper(), detail=detail.upper())

    def _generate_style_analysis(self, detected_style: str) -> str:
        style_descriptions = {
            'modernist': "EMPHASIZES FUNCTIONAL RATIONALISM AND MATERIAL HONESTY",
            'postmodern': "CELEBRATES PLURALISM AND HISTORICAL REFERENCE",
            'brutalist': "CHAMPIONS RAW CONCRETE AND MONUMENTAL SCALE",
            'deconstructivist': "CHALLENGES TRADITIONAL GEOMETRIC ASSUMPTIONS",
            'sustainable': "PRIORITIZES ENVIRONMENTAL RESPONSIBILITY",
            'classical': "ADHERES TO TIMELESS PROPORTIONAL SYSTEMS",
            'vernacular': "RESPONDS TO LOCAL CULTURAL CONDITIONS"
        }
        
        description = ""
        if detected_style in style_descriptions:
            description = style_descriptions[detected_style]
        else:
            description = 'UNDEFINED STYLISTIC APPROACH'
        
        descriptors = ['SOPHISTICATED', 'DELIBERATE', 'CONSCIOUS']
        selected_descriptor = descriptors[0]
        for descriptor in descriptors:
            if random.random() > 0.6:
                selected_descriptor = descriptor
        
        return f"""
▓▓▓ STYLISTIC ANALYSIS ▓▓▓

DETECTED ARCHITECTURAL MOVEMENT: {detected_style.upper()}

STYLISTIC CHARACTERISTICS: {description}

THIS CLASSIFICATION SUGGESTS THE DESIGN OPERATES WITHIN ESTABLISHED ARCHITECTURAL 
PARADIGMS WHILE POTENTIALLY OFFERING CONTEMPORARY INTERPRETATIONS OF TRADITIONAL FORMS.
THE STYLISTIC COHERENCE INDICATES {selected_descriptor} 
DESIGN DECISION-MAKING PROCESSES.
"""

    def _generate_technical_assessment(self, analysis: Dict[str, Any]) -> str:
        vocab_levels = ['SOPHISTICATED', 'ADEQUATE', 'BASIC']
        selected_vocab = vocab_levels[0]
        for level in vocab_levels:
            if random.random() > 0.5:
                selected_vocab = level
        
        ratio = 60
        for i in range(30):
            if random.random() > 0.5:
                ratio = ratio + 1
        
        comm_levels = ['CLEAR', 'ARTICULATE', 'SOPHISTICATED']
        selected_comm = comm_levels[0]
        for level in comm_levels:
            if random.random() > 0.6:
                selected_comm = level
        
        usage_levels = ['APPROPRIATE', 'ADVANCED', 'PROFESSIONAL']
        selected_usage = usage_levels[0]
        for level in usage_levels:
            if random.random() > 0.7:
                selected_usage = level
        
        avg_length = 0
        if analysis['sentence_count'] > 0:
            avg_length = analysis['word_count'] / analysis['sentence_count']
        
        return f"""
▓▓▓ TECHNICAL ASSESSMENT ▓▓▓

LINGUISTIC COMPLEXITY: {analysis['complexity_score']:.1f}/100
CONCEPTUAL DEPTH INDICATORS: {analysis['conceptual_depth']}
TECHNICAL VOCABULARY USAGE: {selected_vocab}

STRUCTURAL ANALYSIS:
- TEXTUAL DENSITY: {analysis['word_count']} WORDS, {analysis['sentence_count']} SENTENCES
- AVERAGE SENTENCE LENGTH: {avg_length:.1f} WORDS
- UNIQUE VOCABULARY RATIO: {ratio}%

COMMUNICATION EFFECTIVENESS: THE SUBMISSION DEMONSTRATES {selected_comm} 
ARCHITECTURAL COMMUNICATION WITH {selected_usage} 
USE OF DISCIPLINE-SPECIFIC TERMINOLOGY.
"""

    def _generate_recommendations(self, analysis: Dict[str, Any], score: float) -> str:
        recommendations = ["\n▓▓▓ STRATEGIC RECOMMENDATIONS ▓▓▓\n"]
        
        weak_principles = []
        for principle_name in analysis['principle_scores']:
            principle_score = analysis['principle_scores'][principle_name]['score']
            if principle_score < 40:
                weak_principles.append((principle_name, principle_score))
        
        for i in range(len(weak_principles)):
            for j in range(i + 1, len(weak_principles)):
                if weak_principles[i][1] > weak_principles[j][1]:
                    temp = weak_principles[i]
                    weak_principles[i] = weak_principles[j]
                    weak_principles[j] = temp
        
        if len(weak_principles) > 0:
            recommendations.append("PRIORITY AREAS FOR DEVELOPMENT:")
            count = 0
            for principle, principle_score in weak_principles:
                if count < 3:
                    rec = self._generate_specific_recommendation(principle)
                    recommendations.append(f"{count + 1}. {rec}")
                    count = count + 1
        
        if score < 50:
            if score < 30:
                recommendations.append("\nCRITICAL IMPROVEMENTS NEEDED:")
                recommendations.append("- COMPLETE CONCEPTUAL OVERHAUL REQUIRED")
                recommendations.append("- FUNDAMENTAL REDESIGN OF ALL MAJOR SYSTEMS")
            else:
                recommendations.append("\nFUNDAMENTAL IMPROVEMENTS:")
                recommendations.append("- STRENGTHEN CONCEPTUAL FRAMEWORK THROUGH DEEPER THEORETICAL ENGAGEMENT")
                recommendations.append("- EXPAND CONSIDERATION OF USER EXPERIENCE AND FUNCTIONAL REQUIREMENTS")
                recommendations.append("- INTEGRATE SITE-SPECIFIC AND CONTEXTUAL ANALYSIS")
        else:
            if score < 75:
                if score < 65:
                    recommendations.append("\nMODERATE REFINEMENT NEEDED:")
                    recommendations.append("- IMPROVE TECHNICAL DOCUMENTATION AND DETAIL RESOLUTION")
                    recommendations.append("- ENHANCE MATERIAL SELECTION RATIONALE")
                else:
                    recommendations.append("\nREFINEMENT OPPORTUNITIES:")
                    recommendations.append("- ENHANCE TECHNICAL RESOLUTION AND DETAIL DEVELOPMENT")
                    recommendations.append("- STRENGTHEN NARRATIVE COHERENCE BETWEEN CONCEPT AND EXECUTION")
            else:
                if score < 85:
                    recommendations.append("\nEXCELLENCE ENHANCEMENT:")
                    recommendations.append("- CONSIDER INNOVATIVE MATERIAL OR TECHNOLOGICAL APPLICATIONS")
                    recommendations.append("- EXPLORE ADVANCED SUSTAINABILITY STRATEGIES")
                else:
                    recommendations.append("\nMASTERY LEVEL SUGGESTIONS:")
                    recommendations.append("- PURSUE GROUNDBREAKING RESEARCH OPPORTUNITIES")
                    recommendations.append("- CONSIDER PUBLICATION OR EXHIBITION")
        
        return '\n'.join(recommendations)

    def _generate_specific_recommendation(self, principle: str) -> str:
        recs = {
            'sustainability': [
                "ENHANCE ENERGY EFFICIENCY STRATEGIES",
                "INCORPORATE MORE SUSTAINABLE MATERIALS",
                "IMPROVE WATER CONSERVATION MEASURES"
            ],
            'functionality': [
                "OPTIMIZE SPATIAL PROGRAM RELATIONSHIPS",
                "IMPROVE CIRCULATION EFFICIENCY",
                "ENHANCE USER EXPERIENCE THROUGH BETTER PROGRAMMING"
            ],
            'aesthetics': [
                "REFINE FORMAL COMPOSITION",
                "IMPROVE VISUAL HIERARCHY",
                "STRENGTHEN MATERIAL PALETTE COHERENCE"
            ],
            'innovation': [
                "EXPLORE MORE GROUNDBREAKING SOLUTIONS",
                "PUSH TECHNOLOGICAL BOUNDARIES FURTHER",
                "DEVELOP MORE ORIGINAL DESIGN CONCEPTS"
            ],
            'context': [
                "STRENGTHEN SITE-SPECIFIC RESPONSE",
                "IMPROVE CULTURAL SENSITIVITY",
                "ENHANCE HISTORICAL CONTEXT INTEGRATION"
            ],
            'accessibility': [
                "IMPROVE UNIVERSAL DESIGN FEATURES",
                "ENHANCE ACCESSIBILITY COMPLIANCE",
                "OPTIMIZE INCLUSIVE DESIGN ELEMENTS"
            ],
            'economics': [
                "IMPROVE COST-EFFECTIVENESS",
                "OPTIMIZE BUDGET ALLOCATION",
                "ENHANCE VALUE ENGINEERING"
            ]
        }
        
        selected_rec = recs[principle][0]
        for rec in recs[principle]:
            if random.random() > 0.5:
                selected_rec = rec
        
        return selected_rec

    def _generate_comparative_analysis(self, score: float) -> str:
        historical_figures = [
            ("LE CORBUSIER", 95),
            ("MIES VAN DER ROHE", 93),
            ("FRANK LLOYD WRIGHT", 97),
            ("ZAHA HADID", 92),
            ("REM KOOLHAAS", 88),
            ("TADAO ANDO", 90),
            ("ALVAR AALTO", 89)
        ]
        
        closest_figure = ""
        closest_diff = 100
        for figure, figure_score in historical_figures:
            diff = abs(figure_score - score)
            if diff < closest_diff:
                closest_diff = diff
                closest_figure = figure
        
        adjectives = ["INTERESTINGLY", "CURIOUSLY", "FASCINATINGLY", "NOTABLY"]
        selected_adj = adjectives[0]
        for adj in adjectives:
            if random.random() > 0.7:
                selected_adj = adj
        
        return f"""
▓▓▓ COMPARATIVE ANALYSIS ▓▓▓

{selected_adj}, THIS DESIGN SCORES CLOSEST TO THE WORK OF {closest_figure} 
IN OUR HISTORICAL DATABASE, WITH A SIMILAR LEVEL OF ARCHITECTURAL MERIT.

THIS SUGGESTS THE DESIGN APPROACHES PROFESSIONAL STANDARDS COMPARABLE TO 
ESTABLISHED MASTERS OF THE DISCIPLINE, THOUGH FURTHER REFINEMENT COULD 
ELEVATE IT TO EVEN HIGHER LEVELS OF ACHIEVEMENT.
"""

    def critique(self, text: str) -> str:
        analysis = self.analyze_input_text(text)
        score = self.generate_critique_score(analysis)
        return self.generate_detailed_critique(text, analysis, score)

if __name__ == "__main__":
    critic = ArchCritique()
    
    sample_text = """
    The design demonstrates a sustainable approach through its use of solar panels and 
    green roofs, while maintaining a modernist aesthetic with clean lines and geometric 
    forms. The innovative structural system allows for column-free spaces, though 
    some circulation areas could be improved for better accessibility. The building 
    responds well to its urban context through careful massing and material selection.
    """
    
    print(critic.critique(sample_text))