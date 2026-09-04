from mcp.server.fastmcp import FastMCP
import psycopg2
import os

mcp = FastMCP("PostgreSQL Secure Client")

@mcp.tool()
def query_database(sql_query: str) -> str:
    """
    Executes a read-only SELECT query against the PostgreSQL database.
    WARNING: Only SELECT statements are permitted.
    """
    if not sql_query.strip().upper().startswith("SELECT"):
        return "Error: Only SELECT queries are permitted via MCP for security reasons."
        
    db_url = os.environ.get("DATABASE_URL")
    if not db_url:
        return "Error: DATABASE_URL environment variable is not set."
        
    try:
        conn = psycopg2.connect(db_url)
        # Ensure read-only transaction
        conn.set_session(readonly=True)
        cur = conn.cursor()
        cur.execute(sql_query)
        rows = cur.fetchall()
        colnames = [desc[0] for desc in cur.description]
        cur.close()
        conn.close()
        
        result = f"| {' | '.join(colnames)} |\n"
        result += f"|{'|'.join(['---'] * len(colnames))}|\n"
        for row in rows:
            result += f"| {' | '.join([str(val) for val in row])} |\n"
            
        return result
    except Exception as e:
        return f"Database Error: {str(e)}"

if __name__ == "__main__":
    mcp.run()
