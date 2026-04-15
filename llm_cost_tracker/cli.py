import argparse
from llm_cost_tracker.tracker import calculate_cost
from llm_cost_tracker.logger import log_usage
from llm_cost_tracker.report import generate_report

def main():
    parser = argparse.ArgumentParser(description="LLM Cost Tracker")

    parser.add_argument("--tokens", type=int, help="Number of tokens used")
    parser.add_argument("--price", type=float, default=0.002, help="Cost per 1000 tokens")
    parser.add_argument("--report", action="store_true", help="Generate usage report")
    parser.add_argument("--today", action="store_true", help="Show today's usage")
    parser.add_argument("--limit", type=float, help="Cost limit alert")
    parser.add_argument("--export", action="store_true", help="Export data to CSV")

    args = parser.parse_args()

    if args.export:
        from llm_cost_tracker.report import export_to_csv
        export_to_csv()
        return
    

    # If user wants report only
    if args.report:
        generate_report()
        return

    if args.today:
        from llm_cost_tracker.report import generate_today_report
        generate_today_report()
        return


    # If tokens are provided
    if args.tokens:
        cost = calculate_cost(args.tokens, args.price)
        log_usage(args.tokens, cost)
        print(f"Cost: ${cost:.6f}")

        if args.limit and cost > args.limit:
            print("⚠️ WARNING: Cost exceeded limit!")


    else:
        print("Please provide --tokens or use --report")

if __name__ == "__main__":
    main()