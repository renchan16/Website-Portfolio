from flask import Blueprint, jsonify

portfolio_bp = Blueprint('portfolio', __name__, url_prefix='/api/portfolio')

@portfolio_bp.route('/', methods=['GET'])
def get_portfolio():
    # This is sample data - replace with your actual data or database integration
    portfolio_data = {
        'name': 'Your Name',
        'title': 'Full Stack Developer',
        'skills': ['JavaScript', 'React', 'Next.js', 'Python', 'Flask', 'Tailwind CSS'],
        'projects': [
            {
                'id': 1,
                'title': 'Project 1',
                'description': 'A description of your first project',
                'technologies': ['Next.js', 'Tailwind CSS', 'Flask'],
                'github': 'https://github.com/yourusername/project1',
                'live': 'https://project1.yourdomain.com'
            },
            {
                'id': 2,
                'title': 'Project 2',
                'description': 'A description of your second project',
                'technologies': ['React', 'Node.js', 'MongoDB'],
                'github': 'https://github.com/yourusername/project2',
                'live': 'https://project2.yourdomain.com'
            }
        ],
        'experience': [
            {
                'id': 1,
                'company': 'Company Name',
                'position': 'Position',
                'duration': 'Month Year - Month Year',
                'description': 'Your responsibilities and achievements'
            }
        ],
        'contact': {
            'email': 'your.email@example.com',
            'linkedin': 'https://linkedin.com/in/yourusername',
            'github': 'https://github.com/yourusername'
        }
    }
    
    return jsonify(portfolio_data)

@portfolio_bp.route('/about', methods=['GET'])
def get_about():
    about_data = {
        'bio': 'Your professional biography goes here.',
        'education': [
            {
                'institution': 'University Name',
                'degree': 'Your Degree',
                'field': 'Your Field of Study',
                'year': '20XX'
            }
        ]
    }
    
    return jsonify(about_data)