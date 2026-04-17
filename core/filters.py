from utils.logger import log_error

def apply_filters(df, agence_filter, segment_filter, produit_filter, year_filter):

    try:
        df = df.copy()

        # --> fix null
        df["agence_nom"] = df["agence_nom"].fillna("Unknown")
        df["segment_nom"] = df["segment_nom"].fillna("Unknown")
        df["produit_nom"] = df["produit_nom"].fillna("Unknown")
        df = df[df["year"].notna()]

        # --> apply filters
        df_filtered = df[
            (df["agence_nom"].isin(agence_filter)) &
            (df["segment_nom"].isin(segment_filter)) &
            (df["produit_nom"].isin(produit_filter)) &
            (df["year"].between(year_filter[0], year_filter[1]))
        ]

        return df_filtered

    except Exception as e:
        log_error(f"Filtering logic error: {str(e)}")
        return df