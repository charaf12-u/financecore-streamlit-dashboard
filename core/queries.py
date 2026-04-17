
# --> requete SQL pour extraire les données
MAIN_QUERY = """
SELECT 
    t.transaction_id,
    t.date_transaction,
    t.montant,
    t.montant_eur,

    c.client_id,
    c.score_credit,
    c.categorie_risque,
    c.taux_interet,

    sc.segment_nom,

    a.agence_nom,

    p.produit_nom,
    cp.categorie_nom,

    d.code_devise,

    st.statut_nom,

    ton.type_operation_nom,

    an.is_anomaly,
    an.is_anomaly_amount,
    an.is_anomaly_score

FROM transaction t

JOIN client c ON t.client_id = c.client_id
JOIN segment_client sc ON c.segment_id = sc.segment_id
JOIN produit p ON t.produit_id = p.produit_id
JOIN categorie_produit cp ON p.categorie_id = cp.categorie_id
JOIN agence a ON t.agence_id = a.agence_id
JOIN devise d ON t.devise_id = d.devise_id
JOIN statut_transaction st ON t.statut_id = st.statut_id
JOIN type_operation ton ON t.type_operation_id = ton.type_operation_id

LEFT JOIN anomalie an ON t.transaction_id = an.transaction_id
"""