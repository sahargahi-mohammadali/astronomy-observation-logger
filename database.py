def save_to_db(df, conn):
    if df.empty:
        print("There is no data to save")
        return

    df.to_sql(
        "observation",
        conn,
        if_exists="replace",
        index=True
    )

    conn.commit()

    print("Data saved to database successfully")