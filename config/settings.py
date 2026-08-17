"""Application settings, color palettes, fonts, and template metadata."""

from typing import Dict, Any

APP_NAME = "ResumeForge"
APP_TAGLINE = "Build beautiful, ATS-friendly, and professional resumes in minutes."

COLOR_PALETTES: Dict[str, Dict[str, str]] = {
    "Navy": {"primary": "#1E3A8A", "secondary": "#3B82F6", "text": "#1F2937", "bg": "#F8FAFC"},
    "Black & White": {"primary": "#111827", "secondary": "#4B5563", "text": "#111827", "bg": "#FFFFFF"},
    "Dark Gray": {"primary": "#374151", "secondary": "#6B7280", "text": "#1F2937", "bg": "#F9FAFB"},
    "Forest Green": {"primary": "#065F46", "secondary": "#10B981", "text": "#064E3B", "bg": "#F0FDF4"},
    "Burgundy": {"primary": "#881337", "secondary": "#F43F5E", "text": "#4C0519", "bg": "#FFF1F2"},
    "Royal Blue": {"primary": "#2563EB", "secondary": "#60A5FA", "text": "#1E293B", "bg": "#EFF6FF"},
    "Teal": {"primary": "#0D9488", "secondary": "#2DD4BF", "text": "#134E4A", "bg": "#F0FDFA"},
    "Purple": {"primary": "#7C3AED", "secondary": "#A78BFA", "text": "#4C1D95", "bg": "#F5F3FF"},
    "Slate": {"primary": "#475569", "secondary": "#94A3B8", "text": "#0F172A", "bg": "#F8FAFC"},
    "Charcoal": {"primary": "#27272A", "secondary": "#71717A", "text": "#18181B", "bg": "#FAFAFA"},
    "Brown": {"primary": "#78350F", "secondary": "#D97706", "text": "#451A03", "bg": "#FEF3C7"},
    "Orange": {"primary": "#C2410C", "secondary": "#FB923C", "text": "#7C2D12", "bg": "#FFF7ED"},
    "Deep Red": {"primary": "#991B1B", "secondary": "#EF4444", "text": "#450A0A", "bg": "#FEF2F2"},
}

FONT_OPTIONS = ["Helvetica", "Times-Roman", "Courier"]

"""50 Unique Resume Template Metadata Definitions for ResumeForge."""

TEMPLATE_METADATA = {
    # 1-10: Modern & Tech
    "tpl_01": {"name": "1. Modern Full-Width Banner", "category": "Modern", "description": "Top color block with a 2-column split."},
    "tpl_02": {"name": "2. Creative Tinted Sidebar", "category": "Creative", "description": "Full-height dark left sidebar (35%)."},
    "tpl_03": {"name": "3. Centered Luxury Serif", "category": "Modern", "description": "Centered title block with elegant rules."},
    "tpl_04": {"name": "4. ATS Plain Machine-Readable", "category": "ATS", "description": "Single-column plain text format."},
    "tpl_05": {"name": "5. Right Sidebar Metadata", "category": "Modern", "description": "Main column left, gray panel right."},
    "tpl_06": {"name": "6. Minimal Clean Grid", "category": "Modern", "description": "Spacious layout with accent borders."},
    "tpl_07": {"name": "7. Corporate Two-Column", "category": "Corporate", "description": "Dense layout for experienced roles."},
    "tpl_08": {"name": "8. Portfolio Showcase", "category": "Creative", "description": "Emphasizes projects and competencies."},
    "tpl_09": {"name": "9. Graduate Entry Focus", "category": "Fresher", "description": "Highlights academic achievements first."},
    "tpl_10": {"name": "10. Compact Grid Minimal", "category": "Modern", "description": "Clean structure for high density."},

    # 11-20: Corporate & Executive
    "tpl_11": {"name": "11. Executive Header Bold", "category": "Corporate", "description": "Dark title block with contrast."},
    "tpl_12": {"name": "12. Bold Accent Highlight", "category": "Creative", "description": "High-contrast section headers."},
    "tpl_13": {"name": "13. Modern Split Columns", "category": "Modern", "description": "50/50 dual column division."},
    "tpl_14": {"name": "14. ATS Corporate Standard", "category": "ATS", "description": "HR-compliant keyword layout."},
    "tpl_15": {"name": "15. Compact Single Column", "category": "Fresher", "description": "Single-page fit for entry-level."},
    "tpl_16": {"name": "16. Legal & Finance Classic", "category": "Corporate", "description": "Serif font, high formality."},
    "tpl_17": {"name": "17. Tech Lead Architecture", "category": "Modern", "description": "Highlights technical leadership."},
    "tpl_18": {"name": "18. Minimal Line Divider", "category": "Modern", "description": "Thin lines separating main blocks."},
    "tpl_19": {"name": "19. Creative Split Navy", "category": "Creative", "description": "Deep blue sidebar with white text."},
    "tpl_20": {"name": "20. Executive Summary First", "category": "Corporate", "description": "Large summary block at top."},

    # 21-30: Creative & Portfolio
    "tpl_21": {"name": "21. Designer Header Badge", "category": "Creative", "description": "Header enclosed in tinted card."},
    "tpl_22": {"name": "22. Developer Project Focus", "category": "Creative", "description": "Displays GitHub and project links."},
    "tpl_23": {"name": "23. Product Manager Grid", "category": "Modern", "description": "Balanced experience and metrics."},
    "tpl_24": {"name": "24. Data Scientist Special", "category": "Modern", "description": "Dedicated section for tech stack."},
    "tpl_25": {"name": "25. Fresher Internship First", "category": "Fresher", "description": "Puts internships above education."},
    "tpl_26": {"name": "26. Student Project Showcase", "category": "Fresher", "description": "Emphasizes coursework and apps."},
    "tpl_27": {"name": "27. Minimal Monogram", "category": "Modern", "description": "Initials icon beside candidate name."},
    "tpl_28": {"name": "28. Corporate Navy Standard", "category": "Corporate", "description": "Traditional navy headers and rules."},
    "tpl_29": {"name": "29. ATS Tech Keyword Dense", "category": "ATS", "description": "Optimized for automated screening."},
    "tpl_30": {"name": "30. Full Page Two-Tone", "category": "Creative", "description": "Shaded background panels."},

    # 31-40: Fresher & Entry Level
    "tpl_31": {"name": "31. Academic Scholar", "category": "Fresher", "description": "Highlights GPA, honors, and thesis."},
    "tpl_32": {"name": "32. Modern Teal Accent", "category": "Modern", "description": "Teal section headers and borders."},
    "tpl_33": {"name": "33. Charcoal Executive", "category": "Corporate", "description": "Slate-gray header banner."},
    "tpl_34": {"name": "34. Clean Sans-Serif Minimal", "category": "Modern", "description": "Helvetica typography with clean spacing."},
    "tpl_35": {"name": "35. Creative Purple Tint", "category": "Creative", "description": "Purple left panel for creative roles."},
    "tpl_36": {"name": "36. ATS Minimal Mono", "category": "ATS", "description": "Monospaced clean layout for ATS."},
    "tpl_37": {"name": "37. Banking & Finance Pro", "category": "Corporate", "description": "Structured layout for banking roles."},
    "tpl_38": {"name": "38. Full-Width Border Rule", "category": "Modern", "description": "Thick colored bar under header."},
    "tpl_39": {"name": "39. Asymmetric Sidebar", "category": "Creative", "description": "30% left column, 70% right column."},
    "tpl_40": {"name": "40. Executive Two-Page Ready", "category": "Corporate", "description": "Budgeted for multi-page resumes."},

    # 41-50: Advanced Custom Layouts
    "tpl_41": {"name": "41. Forest Green Accent", "category": "Modern", "description": "Green headers for environmental/management."},
    "tpl_42": {"name": "42. Burgundy Serif Luxury", "category": "Corporate", "description": "Burgundy headers with Times font."},
    "tpl_43": {"name": "43. High-Density One Page", "category": "Fresher", "description": "Compact padding to fit everything on 1 page."},
    "tpl_44": {"name": "44. Tech Stack Pill Grid", "category": "Creative", "description": "Highlights skills in organized blocks."},
    "tpl_45": {"name": "45. Minimalist Centered Header", "category": "Modern", "description": "Clean centered contact details."},
    "tpl_46": {"name": "46. Corporate Standard Black", "category": "Corporate", "description": "High-contrast black & white style."},
    "tpl_47": {"name": "47. ATS Developer Standard", "category": "ATS", "description": "Plain single-column for tech roles."},
    "tpl_48": {"name": "48. Creative Gradient Header", "category": "Creative", "description": "Modern colored banner with full details."},
    "tpl_49": {"name": "49. Executive Consultant", "category": "Corporate", "description": "Tailored for senior consulting roles."},
    "tpl_50": {"name": "50. Modern Universal Standard", "category": "Modern", "description": "Balanced default layout for any domain."}
}