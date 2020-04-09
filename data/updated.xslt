<?xml version="1.0"?>

<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
  <html>
  <body>
    <h2>Phone list</h2>
    <table border="1">
      <tr bgcolor="#9acd32">
        <th>ID</th>
        <th>Model name</th>
		<th>Company name</th>
		<th>Price</th>
		<th>Rating</th>
		<th>Amount of customers</th>
		<th>Country name</th>
      </tr>
      <xsl:for-each select="items_list/phone">
        <tr>
			<td><xsl:value-of select="@id"/></td>
            <td><xsl:value-of select="model_name"/></td>
          	<td><xsl:value-of select="company_name"/></td>
			<td>
                <xsl:value-of select="price"/>
                <br/>
                <xsl:value-of select="price/@currency"/>s
            </td>
			<td><xsl:value-of select="rating"/></td>
			<td>
                <xsl:value-of select="amount_of_customers"/>
                <br/>
                <xsl:value-of select="amount_of_customers/@currency"/>
            </td>
			<td><xsl:value-of select="country/name"/></td>
        </tr>
      </xsl:for-each>
    </table>
  </body>
  </html>
</xsl:template>

</xsl:stylesheet>