import argparse
from llm_cost_tracker.tracker import calculate_cost
from llm_cost_tracker.logger import log_usage
from llm_cost_tracker.report import generate_report

def main():
    parser = argparse.ArgumentParser(description="LLM Cost Tracker")

    parser.add_argument("--tokens", type=int, help="Number of tokens used")
    parser.add_argument("--price", type=float, default=0.002, help="Cost per 1000 tokens")
    parser.add_argument("--report", action="store_true", help="Generate usage report")

    args = parser.parse_args()

    # If user wants report only
    if args.report:
        generate_report()
        return

    # If tokens are provided
    if args.tokens:
        cost = calculate_cost(args.tokens, args.price)
        log_usage(args.tokens, cost)
        print(f"Cost: ${cost:.6f}")
    else:
        print("Please provide --tokens or use --report")

if __name__ == "__main__":
    main()