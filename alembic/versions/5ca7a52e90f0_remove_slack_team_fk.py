"""remove slack team fk

Revision ID: 5ca7a52e90f0
Revises: fdce925467c7
Create Date: 2025-01-15 19:20:19.663174

"""

from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "5ca7a52e90f0"
down_revision: Union[str, None] = "fdce925467c7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(
        "slack_users_slack_team_id_fkey", "slack_users", type_="foreignkey"
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    # drop all slack_user records
    op.execute("DELETE FROM slack_users")
    op.create_foreign_key(
        "slack_users_slack_team_id_fkey",
        "slack_users",
        "slack_spaces",
        ["slack_team_id"],
        ["team_id"],
    )
    # ### end Alembic commands ###
