from utils import connections, funcs

def update_permissions(schema, table_name, conn):
    statement = f'GRANT SELECT ON TABLE {schema}.{table_name} TO GROUP sf_data_analysts'
    conn.execute(statement)

if __name__ == "__main__":
    rs_creds = funcs.generate_creds_from_path(**funcs.get_secret('legacy-redshift'))
    rs_con = connections.sa_connection(**rs_creds)
    update_permissions('analysts_playground', 'sfmc_daily_global_email_report', conn)
