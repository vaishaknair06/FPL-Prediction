from src.data_loader import load_fpl_data

def main():
    df = load_fpl_data()
    print("Top 5 Players:")
    print(df[['first_name', 'second_name', 'form', 'total_points']].head())

if __name__ == "__main__":
    main()
