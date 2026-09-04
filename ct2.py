#!/usr/bin/env python3
"""
YourLastName Adaptive Model - A hybrid software development process model
Combines Waterfall structure with Scrum iterations and Spiral risk management
"""

def display_banner():
    """Display the model introduction banner"""
    print("=" * 70)
    print("  YourLastName Adaptive Model")
    print("  A Hybrid Approach: Waterfall + Scrum + Spiral")
    print("=" * 70)
    print()
    print("This model combines:")
    print("  • Waterfall's structured phases")
    print("  • Scrum's iterative sprints and customer collaboration")
    print("  • Spiral's risk assessment and prototyping")
    print()
    print("=" * 70)
    print()

def get_phase_info():
    """Prompt user for phase information and return a list of phases"""
    phases = []
    
    print("Enter information for each phase of your development model.")
    print("Press Enter with an empty phase name to finish.\n")
    
    phase_number = 1
    
    while True:
        print(f"--- Phase {phase_number} ---")
        phase_name = input(f"Phase {phase_number} name (or press Enter to finish): ").strip()
        
        if not phase_name:
            if phase_number == 1:
                print("Error: You must enter at least one phase.")
                continue
            else:
                break
        
        phase_description = input(f"Description for '{phase_name}': ").strip()
        
        if not phase_description:
            phase_description = "No description provided"
        
        phases.append({
            'number': phase_number,
            'name': phase_name,
            'description': phase_description
        })
        
        phase_number += 1
        print()
    
    return phases

def display_model_summary(phases):
    """Display a formatted summary of the model phases"""
    print("\n" + "=" * 70)
    print("  MODEL SUMMARY")
    print("=" * 70)
    print()
    
    for phase in phases:
        print(f"Phase {phase['number']}: {phase['name']}")
        print(f"  → {phase['description']}")
        print()
    
    print("=" * 70)
    print("\nKey Adaptive Features:")
    print("  ✓ Customer feedback loops after each phase")
    print("  ✓ Sprint-based iterations within implementation phases")
    print("  ✓ Risk assessment checkpoints")
    print("  ✓ Continuous integration and testing")
    print("  ✓ Ability to revisit previous phases based on feedback")
    print("=" * 70)

def display_default_model():
    """Display a pre-configured example of the adaptive model"""
    try:
        print("\nWould you like to see a pre-configured example? (yes/no): ", end='')
        choice = input().strip().lower()
    except EOFError:
        choice = 'yes'
    
    if choice in ['yes', 'y', '']:
        example_phases = [
            {
                'number': 1,
                'name': 'Discovery & Requirements',
                'description': 'Requirements and risk identification'
            },
            {
                'number': 2,
                'name': 'Iterative Planning',
                'description': 'Sprint planning and backlog creation'
            },
            {
                'number': 3,
                'name': 'Incremental Design & Prototyping',
                'description': 'Architecture and validation'
            },
            {
                'number': 4,
                'name': 'Sprint-Based Development',
                'description': 'Iterative implementation - Cycles through Phases 2 & 3 until customer approval'
            },
            {
                'number': 5,
                'name': 'Continuous Validation',
                'description': 'Ongoing testing and QA'
            },
            {
                'number': 6,
                'name': 'Adaptive Deployment',
                'description': 'Phased rollout with monitoring'
            },
            {
                'number': 7,
                'name': 'Maintenance & Evolution',
                'description': 'Support and continuous improvement'
            }
        ]
        
        print("\n" + "=" * 70)
        print("  EXAMPLE: YourLastName Adaptive Model")
        print("=" * 70)
        print()
        
        for phase in example_phases:
            print(f"Phase {phase['number']}: {phase['name']}")
            print(f"  → {phase['description']}")
            print()
        
        print("=" * 70)
        print("\nAdaptive Features in This Model:")
        print("  • Feedback Loops: Customer reviews after each phase")
        print("  • Planning-Design Iteration: Phases 2 & 3 cycle until customer approval")
        print("  • Sprints: 2-4 week iterations in development phases")
        print("  • Risk Management: Continuous risk assessment (Spiral approach)")
        print("  • Flexibility: Ability to return to previous phases")
        print("  • Incremental Delivery: Release features progressively")
        print("=" * 70)

def main():
    """Main function to run the adaptive model interface"""
    display_banner()
    
    print("Choose an option:")
    print("1. Create your own custom model")
    print("2. View example model only")
    print("3. Both")
    print()
    
    choice = input("Enter choice (1/2/3): ").strip()
    print()
    
    if choice == '1':
        phases = get_phase_info()
        display_model_summary(phases)
    elif choice == '2':
        display_default_model()
    elif choice == '3':
        display_default_model()
        print("\n\nNow create your own custom model:\n")
        phases = get_phase_info()
        display_model_summary(phases)
    else:
        print("Invalid choice. Running default example...")
        display_default_model()

if __name__ == "__main__":
    main()