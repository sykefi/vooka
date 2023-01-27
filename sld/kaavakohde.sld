<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" version="1.1.0" xsi:schemaLocation="http://www.opengis.net/sld http://schemas.opengis.net/sld/1.1.0/StyledLayerDescriptor.xsd"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:xlink="http://www.w3.org/1999/xlink"
  xmlns:ogc="http://www.opengis.net/ogc"
  xmlns:se="http://www.opengis.net/se">
  <NamedLayer>
    <se:Name>Kaavakohde</se:Name>
    <!-- Flatten view structure, not according to complex structure -->
    <UserStyle>
      <se:Name>Kaavakohde</se:Name>
      <se:FeatureTypeStyle>

        <se:Rule>          <!-- MRL AK 1 | MRL YK 27-->
          <se:Name>Asumisen alue</se:Name>
          <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>asumisenAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>lisatiedonlaji</ogc:PropertyName>
                <ogc:Literal>paaKayttoTarkoitus</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:And>
          </ogc:Filter>
          <se:PolygonSymbolizer>
            <se:Fill>
              <se:SvgParameter name="fill">#e2c096</se:SvgParameter>
            </se:Fill>
            <se:Stroke>
              <se:SvgParameter name="stroke">#000000</se:SvgParameter>
              <se:SvgParameter name="stroke-width">4</se:SvgParameter>
              <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
            </se:Stroke>
          </se:PolygonSymbolizer>
          <se:TextSymbolizer>
            <se:Label>
              <ogc:Literal>A</ogc:Literal>
            </se:Label>
            <se:Font>
              <se:SvgParameter name="font-family">Arial</se:SvgParameter>
              <se:SvgParameter name="font-size">29</se:SvgParameter>
              <se:SvgParameter name="font-style">normal</se:SvgParameter>
              <se:SvgParameter name="font-weight">bold</se:SvgParameter>
            </se:Font>
          </se:TextSymbolizer>
        </se:Rule>

        <se:Rule>          <!-- MRL AK 3 | MRL YK 29 -->
          <se:Name>Asuinpientaloalue alue</se:Name>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>laji</ogc:PropertyName>
              <ogc:Literal>asuinPientaloAlue</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:PolygonSymbolizer>
            <se:Fill>
              <se:SvgParameter name="fill">#e2c096</se:SvgParameter>
            </se:Fill>
            <se:Stroke>
              <se:SvgParameter name="stroke">#000000</se:SvgParameter>
              <se:SvgParameter name="stroke-width">4</se:SvgParameter>
              <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
            </se:Stroke>
          </se:PolygonSymbolizer>
          <se:TextSymbolizer>
            <se:Label>Ap</se:Label>
            <se:Font>
              <se:SvgParameter name="font-family">Arial</se:SvgParameter>
              <se:SvgParameter name="font-size">29</se:SvgParameter>
              <se:SvgParameter name="font-style">normal</se:SvgParameter>
              <se:SvgParameter name="font-weight">bold</se:SvgParameter>
            </se:Font>
          </se:TextSymbolizer>
        </se:Rule>

        <se:Rule>          <!-- MRL AK 5 -->
          <se:Name>Erillisten asuinpientalojen alue</se:Name>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>laji</ogc:PropertyName>
              <ogc:Literal>erillistenAsuinpienTalojenAlue</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:PolygonSymbolizer>
            <se:Fill>
              <se:SvgParameter name="fill">#e2c096</se:SvgParameter>
            </se:Fill>
            <se:Stroke>
              <se:SvgParameter name="stroke">#000000</se:SvgParameter>
              <se:SvgParameter name="stroke-width">4</se:SvgParameter>
              <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
            </se:Stroke>
          </se:PolygonSymbolizer>
          <se:TextSymbolizer>
            <se:Label>Ao</se:Label>
            <se:Font>
              <se:SvgParameter name="font-family">Arial</se:SvgParameter>
              <se:SvgParameter name="font-size">29</se:SvgParameter>
              <se:SvgParameter name="font-style">normal</se:SvgParameter>
              <se:SvgParameter name="font-weight">bold</se:SvgParameter>
            </se:Font>
          </se:TextSymbolizer>
        </se:Rule>

        <se:Rule>          <!-- MRL AK 2 | MRL YK 28 -->
          <se:Name>Asuinkerrostaloalue</se:Name>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>laji</ogc:PropertyName>
              <ogc:Literal>asuinKerrostaloAlue</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:PolygonSymbolizer>
            <se:Fill>
              <se:SvgParameter name="fill">#b98444</se:SvgParameter>
            </se:Fill>
            <se:Stroke>
              <se:SvgParameter name="stroke">#000000</se:SvgParameter>
              <se:SvgParameter name="stroke-width">4</se:SvgParameter>
              <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
            </se:Stroke>
          </se:PolygonSymbolizer>
          <se:TextSymbolizer>
            <se:Label>Ak</se:Label>
            <se:Font>
              <se:SvgParameter name="font-family">Arial</se:SvgParameter>
              <se:SvgParameter name="font-size">29</se:SvgParameter>
              <se:SvgParameter name="font-style">normal</se:SvgParameter>
              <se:SvgParameter name="font-weight">bold</se:SvgParameter>
            </se:Font>
          </se:TextSymbolizer>
        </se:Rule>

        <se:Rule>          <!-- MRL AK 4 | MRL YK 27 -->
          <se:Name>Rivitalojen ja muiden kytkettyjen asuinpientalojen alue</se:Name>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>laji</ogc:PropertyName>
              <ogc:Literal>rivitalojenJaMuidenKytkettyjenAsuinpientalojenAlue</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:PolygonSymbolizer>
            <se:Fill>
              <se:SvgParameter name="fill">#e2c096</se:SvgParameter>
            </se:Fill>
            <se:Stroke>
              <se:SvgParameter name="stroke">#000000</se:SvgParameter>
              <se:SvgParameter name="stroke-width">4</se:SvgParameter>
              <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
            </se:Stroke>
          </se:PolygonSymbolizer>
          <se:TextSymbolizer>
            <se:Label>Ar</se:Label>
            <se:Font>
              <se:SvgParameter name="font-family">Arial</se:SvgParameter>
              <se:SvgParameter name="font-size">29</se:SvgParameter>
              <se:SvgParameter name="font-style">normal</se:SvgParameter>
              <se:SvgParameter name="font-weight">bold</se:SvgParameter>
            </se:Font>
          </se:TextSymbolizer>
        </se:Rule>

        <se:Rule>          <!-- MRL AK 7 -->
          <se:Name>Asumista palveleva yhteiskäyttöinen alue</se:Name>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>laji</ogc:PropertyName>
              <ogc:Literal>asumistaPalvelevaYhteiskayttoinenAlue</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:PolygonSymbolizer>
            <se:Fill>
              <se:SvgParameter name="fill">#e2c096</se:SvgParameter>
            </se:Fill>
            <se:Stroke>
              <se:SvgParameter name="stroke">#000000</se:SvgParameter>
              <se:SvgParameter name="stroke-width">4</se:SvgParameter>
              <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
            </se:Stroke>
          </se:PolygonSymbolizer>
          <se:TextSymbolizer>
            <se:Label>Ah</se:Label>
            <se:Font>
              <se:SvgParameter name="font-family">Arial</se:SvgParameter>
              <se:SvgParameter name="font-size">29</se:SvgParameter>
              <se:SvgParameter name="font-style">normal</se:SvgParameter>
              <se:SvgParameter name="font-weight">bold</se:SvgParameter>
            </se:Font>
          </se:TextSymbolizer>
        </se:Rule>

        <se:Rule>          <!-- MRL AK 8 -->
          <se:Name>Maatilan talouskeskuksen alue</se:Name>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>laji</ogc:PropertyName>
              <ogc:Literal>maatilanTalouskeskuksenAlue</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:PolygonSymbolizer>
            <se:Fill>
              <se:SvgParameter name="fill">#e2c096</se:SvgParameter>
            </se:Fill>
            <se:Stroke>
              <se:SvgParameter name="stroke">#000000</se:SvgParameter>
              <se:SvgParameter name="stroke-width">4</se:SvgParameter>
              <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
            </se:Stroke>
          </se:PolygonSymbolizer>
          <se:TextSymbolizer>
            <se:Label>Am</se:Label>
            <se:Font>
              <se:SvgParameter name="font-family">Arial</se:SvgParameter>
              <se:SvgParameter name="font-size">29</se:SvgParameter>
              <se:SvgParameter name="font-style">normal</se:SvgParameter>
              <se:SvgParameter name="font-weight">bold</se:SvgParameter>
            </se:Font>
          </se:TextSymbolizer>
        </se:Rule>

        <se:Rule>          <!-- MRL YK 30 -->
          <se:Name>Kyläalue</se:Name>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>laji</ogc:PropertyName>
              <ogc:Literal>kylaAlue</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:PolygonSymbolizer>
            <se:Fill>
              <se:SvgParameter name="fill">#e2c096</se:SvgParameter>
            </se:Fill>
            <se:Stroke>
              <se:SvgParameter name="stroke">#000000</se:SvgParameter>
              <se:SvgParameter name="stroke-width">4</se:SvgParameter>
              <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
            </se:Stroke>
          </se:PolygonSymbolizer>
          <se:TextSymbolizer>
            <se:Label>AT</se:Label>
            <se:Font>
              <se:SvgParameter name="font-family">Arial</se:SvgParameter>
              <se:SvgParameter name="font-size">29</se:SvgParameter>
              <se:SvgParameter name="font-style">normal</se:SvgParameter>
              <se:SvgParameter name="font-weight">bold</se:SvgParameter>
            </se:Font>
          </se:TextSymbolizer>
        </se:Rule>

        <se:Rule>          <!-- MRL AK 6 -->
          <se:Name>Asuin-, liike- ja toimistorakennusten alue</se:Name>
          <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsLike escapeChar="\" wildCard='%' singleChar='*'>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>asumisenAlue</ogc:Literal>
              </ogc:PropertyIsLike>
              <ogc:PropertyIsLike escapeChar="\" wildCard='%' singleChar='*'>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>liikerakennustenAlue</ogc:Literal>
              </ogc:PropertyIsLike>
            </ogc:And>
            <ogc:Or>
              <ogc:And>
                <ogc:PropertyIsLike escapeChar="\" wildCard='%' singleChar='*'>
                  <ogc:PropertyName>laji</ogc:PropertyName>
                  <ogc:Literal>asumisenAlue</ogc:Literal>
                </ogc:PropertyIsLike>
                <ogc:PropertyIsLike escapeChar="\" wildCard='%' singleChar='*'>
                  <ogc:PropertyName>laji</ogc:PropertyName>
                  <ogc:Literal>toimistorakennustenAlue</ogc:Literal>
                </ogc:PropertyIsLike>
              </ogc:And>
            </ogc:Or>
          </ogc:Filter>
          <se:PolygonSymbolizer>
            <se:Fill>
              <se:SvgParameter name="fill">#b98444</se:SvgParameter>
            </se:Fill>
            <se:Stroke>
              <se:SvgParameter name="stroke">#000000</se:SvgParameter>
              <se:SvgParameter name="stroke-width">4</se:SvgParameter>
              <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
            </se:Stroke>
          </se:PolygonSymbolizer>
          <se:TextSymbolizer>
            <se:Label>Al</se:Label>
            <se:Font>
              <se:SvgParameter name="font-family">Arial</se:SvgParameter>
              <se:SvgParameter name="font-size">29</se:SvgParameter>
              <se:SvgParameter name="font-style">normal</se:SvgParameter>
              <se:SvgParameter name="font-weight">bold</se:SvgParameter>
            </se:Font>
          </se:TextSymbolizer>
        </se:Rule>

        <se:Rule>          <!-- MRL AK 9 -->
          <se:Name>Palvelurakennusten alue</se:Name>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>laji</ogc:PropertyName>
              <ogc:Literal>palvelurakennustenAlue</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:PolygonSymbolizer>
            <se:Fill>
              <se:SvgParameter name="fill">#faab53</se:SvgParameter>
            </se:Fill>
            <se:Stroke>
              <se:SvgParameter name="stroke">#000000</se:SvgParameter>
              <se:SvgParameter name="stroke-width">4</se:SvgParameter>
              <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
            </se:Stroke>
          </se:PolygonSymbolizer>
          <se:TextSymbolizer>
            <se:Label>P</se:Label>
            <se:Font>
              <se:SvgParameter name="font-family">Arial</se:SvgParameter>
              <se:SvgParameter name="font-size">29</se:SvgParameter>
              <se:SvgParameter name="font-style">normal</se:SvgParameter>
              <se:SvgParameter name="font-weight">bold</se:SvgParameter>
            </se:Font>
          </se:TextSymbolizer>
        </se:Rule>

        <se:Rule>          <!-- MRL AK 10 -->
          <se:Name>Lähipalvelujen alue</se:Name>
          <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsEqualTo>
                <ogc:Function name="dimension">
                  <ogc:PropertyName>geom</ogc:PropertyName>
                </ogc:Function>
                <ogc:Literal>2</ogc:Literal>
              </ogc:PropertyIsEqualTo>
              <ogc:And>
                <ogc:PropertyIsEqualTo>
                  <ogc:PropertyName>laji</ogc:PropertyName>
                  <ogc:Literal>palvelurakennustenAlue</ogc:Literal>
                </ogc:PropertyIsEqualTo>
                <ogc:PropertyIsEqualTo>
                  <ogc:PropertyName>lisatieto</ogc:PropertyName>
                  <ogc:Literal>paikallinen</ogc:Literal>
                </ogc:PropertyIsEqualTo>
              </ogc:And>
            </ogc:And>
          </ogc:Filter>
          <se:PolygonSymbolizer>
            <se:Fill>
              <se:SvgParameter name="fill">#faab53</se:SvgParameter>
            </se:Fill>
            <se:Stroke>
              <se:SvgParameter name="stroke">#000000</se:SvgParameter>
              <se:SvgParameter name="stroke-width">4</se:SvgParameter>
              <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
            </se:Stroke>
          </se:PolygonSymbolizer>
          <se:TextSymbolizer>
            <se:Label>Pl</se:Label>
            <se:Font>
              <se:SvgParameter name="font-family">Arial</se:SvgParameter>
              <se:SvgParameter name="font-size">29</se:SvgParameter>
              <se:SvgParameter name="font-style">normal</se:SvgParameter>
              <se:SvgParameter name="font-weight">bold</se:SvgParameter>
            </se:Font>
          </se:TextSymbolizer>
        </se:Rule>

        <se:Rule>          <!-- MRL YK 85 -->
          <se:Name>Lähipalvelujen alue</se:Name>
          <ogc:Filter>
            <ogc:And>
              <ogc:And>
                <ogc:PropertyIsEqualTo>
                  <ogc:Function name="dimension">
                    <ogc:PropertyName>geom</ogc:PropertyName>
                  </ogc:Function>
                  <ogc:Literal>0</ogc:Literal>
                </ogc:PropertyIsEqualTo>
                <ogc:PropertyIsEqualTo>
                  <ogc:PropertyName>laji</ogc:PropertyName>
                  <ogc:Literal>keskustaToimintojenAlakeskus</ogc:Literal>
                </ogc:PropertyIsEqualTo>
              </ogc:And>
              <ogc:And>
                <ogc:PropertyIsEqualTo>
                  <ogc:PropertyName>laji</ogc:PropertyName>
                  <ogc:Literal>palvelurakennustenAlue</ogc:Literal>
                </ogc:PropertyIsEqualTo>
                <ogc:PropertyIsEqualTo>
                  <ogc:PropertyName>lisatieto</ogc:PropertyName>
                  <ogc:Literal>paikallinen</ogc:Literal>
                </ogc:PropertyIsEqualTo>
              </ogc:And>
            </ogc:And>
          </ogc:Filter>
          <se:MaxScaleDenominator>80000</se:MaxScaleDenominator>
          <se:PointSymbolizer>
            <se:Graphic>
              <se:Mark>
                <se:WellKnownName>circle</se:WellKnownName>
                <se:Fill>
                  <se:SvgParameter name="fill">#faab53</se:SvgParameter>
                </se:Fill>
                <se:Stroke>
                  <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                  <se:SvgParameter name="stroke-width">1.5</se:SvgParameter>
                </se:Stroke>
              </se:Mark>
              <se:Size>29</se:Size>
            </se:Graphic>
          </se:PointSymbolizer>
          <se:TextSymbolizer>
            <se:Label>
                pl           
            </se:Label>
            <se:Font>
              <se:SvgParameter name="font-family">Arial</se:SvgParameter>
              <se:SvgParameter name="font-size">15</se:SvgParameter>
              <se:SvgParameter name="font-style">normal</se:SvgParameter>
              <se:SvgParameter name="font-weight">normal</se:SvgParameter>
            </se:Font>
            <se:LabelPlacement>
              <se:PointPlacement>
                <se:Displacement>
                  <se:DisplacementX>-8</se:DisplacementX>
                  <se:DisplacementY>0</se:DisplacementY>
                </se:Displacement>
              </se:PointPlacement>
            </se:LabelPlacement>
          </se:TextSymbolizer>
        </se:Rule>

        <se:Rule>          <!-- MRL AK 11 -->
          <se:Name>Huvi- ja viihepalvelujen rakennusten alue</se:Name>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>laji</ogc:PropertyName>
              <ogc:Literal>huviJaViihdePalvelujenRakennustenAlue</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:PolygonSymbolizer>
            <se:Fill>
              <se:SvgParameter name="fill">#faab53</se:SvgParameter>
            </se:Fill>
            <se:Stroke>
              <se:SvgParameter name="stroke">#000000</se:SvgParameter>
              <se:SvgParameter name="stroke-width">4</se:SvgParameter>
              <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
            </se:Stroke>
          </se:PolygonSymbolizer>
          <se:TextSymbolizer>
            <se:Label>Pv</se:Label>
            <se:Font>
              <se:SvgParameter name="font-family">Arial</se:SvgParameter>
              <se:SvgParameter name="font-size">29</se:SvgParameter>
              <se:SvgParameter name="font-style">normal</se:SvgParameter>
              <se:SvgParameter name="font-weight">bold</se:SvgParameter>
            </se:Font>
          </se:TextSymbolizer>
        </se:Rule>

        <se:Rule>          <!-- MRL AK 12 -->
          <se:Name>Yleisten rakennusten alue</se:Name>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>laji</ogc:PropertyName>
              <ogc:Literal>yleistenRakennustenAlue</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:PolygonSymbolizer>
            <se:Fill>
              <se:SvgParameter name="fill">#ddd4e9</se:SvgParameter>
            </se:Fill>
            <se:Stroke>
              <se:SvgParameter name="stroke">#000000</se:SvgParameter>
              <se:SvgParameter name="stroke-width">4</se:SvgParameter>
              <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
            </se:Stroke>
          </se:PolygonSymbolizer>
          <se:TextSymbolizer>
            <se:Label>Y</se:Label>
            <se:Font>
              <se:SvgParameter name="font-family">Arial</se:SvgParameter>
              <se:SvgParameter name="font-size">29</se:SvgParameter>
              <se:SvgParameter name="font-style">normal</se:SvgParameter>
              <se:SvgParameter name="font-weight">bold</se:SvgParameter>
            </se:Font>
          </se:TextSymbolizer>
        </se:Rule>

        <se:Rule>          <!-- MRL AK 13 -->

          <se:Name>Julkisten lähipalvelurakennusten alue</se:Name>
          <ogc:And>
            <ogc:And>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>palvelurakennustenAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>lisatieto</ogc:PropertyName>
                <ogc:Literal>varattuYleiseenKayttoon</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:And>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>lisatieto</ogc:PropertyName>
              <ogc:Literal>paikallinen</ogc:Literal>
            </ogc:PropertyIsEqualTo>
            <ogc:And>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#ddd4e9</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>YL</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>
            <se:Name>Hallintorakennusten alue</se:Name>
            <!-- MRL AK 14 -->
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>hallintoRakennustenAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#ddd4e9</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>YH</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>
            <se:Name>Opetusrakennusten alue</se:Name>
            <!-- MRL AK 15 -->
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>opetusrakennustenAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#ddd4e9</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>YO</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>
            <se:Name>Hoitoalan rakennusten alue</se:Name>
            <!-- MRL AK 16 -->
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>hoitoalanRakennustenAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#ddd4e9</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>YS</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>
            <se:Name>Kulttuurirakennusten alue</se:Name>
            <!-- MRL AK 17 -->
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>kulttuuriRakennustenAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#ddd4e9</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>YY</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>
            <se:Name>Museorakennusten alue</se:Name>
            <!-- MRL AK 18 -->
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>museoRakennustenAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#ddd4e9</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>YM</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>
            <se:Name>Uskonnollisten yhteisöjen rakennusten alue</se:Name>
            <!-- MRL AK 19 -->
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>uskonnollistenYhteistojenRakennustenAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#ddd4e9</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>YK</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>
            <se:Name>Urheilu- ja liikuntarakennusten alue</se:Name>
            <!-- MRL AK 20 -->
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>urheiluJaLiikuntaRakennustenAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#ddd4e9</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>YU</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>
            <se:Name>Keskustatoimintojen alue</se:Name>
            <!-- MRL AK 21 | MRL YK 31 -->
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>keskustaToimintojenAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#d63648</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>C</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>
            <se:Name>Keskustatoimintojen alakeskus</se:Name>
            <!-- MRL YK 84 -->
            <ogc:Filter>
              <ogc:And>
                <ogc:PropertyIsEqualTo>
                  <ogc:Function name="dimension">
                    <ogc:PropertyName>geom</ogc:PropertyName>
                  </ogc:Function>
                  <ogc:Literal>0</ogc:Literal>
                </ogc:PropertyIsEqualTo>
                <ogc:PropertyIsEqualTo>
                  <ogc:PropertyName>laji</ogc:PropertyName>
                  <ogc:Literal>keskustaToimintojenAlakeskus</ogc:Literal>
                </ogc:PropertyIsEqualTo>
              </ogc:And>
            </ogc:Filter>
            <se:PointSymbolizer>
              <se:Graphic>
                <se:Mark>
                  <se:WellKnownName>circle</se:WellKnownName>
                  <se:Fill>
                    <se:SvgParameter name="fill">#d63648</se:SvgParameter>
                  </se:Fill>
                  <se:Stroke>
                    <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                    <se:SvgParameter name="stroke-width">1.5</se:SvgParameter>
                  </se:Stroke>
                </se:Mark>
                <se:Size>29</se:Size>
              </se:Graphic>
            </se:PointSymbolizer>
            <se:TextSymbolizer>
              <se:Label>
                ca         
              </se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">15</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">normal</se:SvgParameter>
              </se:Font>
              <se:LabelPlacement>
                <se:PointPlacement>
                  <se:Displacement>
                    <se:DisplacementX>-8</se:DisplacementX>
                    <se:DisplacementY>-4</se:DisplacementY>
                  </se:Displacement>
                </se:PointPlacement>
              </se:LabelPlacement>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>
            <se:Name>Toimitilojen alue</se:Name>
            <!-- MRL AK 22 -->
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>toimiTilojenAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#faab53</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>K</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>
            <se:Name>Liikerakennusten alue</se:Name>
            <!-- MRL AK 23 -->
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>liikerakennustenAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#faab53</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>KL</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>
            <se:Name>Vähittäiskaupan suuryksikkö</se:Name>
            <!-- MRL AK 24 | MRL YK 32 -->
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>vahittaiskaupanSuuryksikko</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#faab53</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>KM</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>
            <se:Name>Toimistorakennusten alue</se:Name>
            <!-- MRL AK 25 | MRL YK 36 -->
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>toimistorakennustenAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#faab53</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>KT</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>
            <se:Name>Tuotantorakennusten alue</se:Name>
            <!-- MRL AK 27 | MRL YK 37 -->
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>tuotantoRakennustenAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#c1c3c5</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>T</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>
            <se:Name>Varastorakennusten alue</se:Name>
            <!-- MRL AK 29 | MRL YK 40 -->
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>varastoRakennustenAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#c1c3c5</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>TV</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>
            <se:Name>Tuotantorakennusten alue, jolla ympäristö asettaa toiminnan laadulle erityisiä vaatimuksia</se:Name>
            <!-- MRL AK 30 | MRL YK 39 -->
            <ogc:Filter>
              <ogc:And>
                <ogc:PropertyIsLike escapeChar="\" wildCard='%' singleChar='*'>
                  <ogc:PropertyName>laji</ogc:PropertyName>
                  <ogc:Literal>tuotantorakennustenAlue</ogc:Literal>
                </ogc:PropertyIsLike>
                <ogc:PropertyIsLike escapeChar="\" wildCard='%' singleChar='*'>
                  <ogc:PropertyName>laji</ogc:PropertyName>
                  <ogc:Literal>ymparistoarvojenHuomioiminen</ogc:Literal>
                </ogc:PropertyIsLike>
              </ogc:And>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#c1c3c5</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>TY</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsLike escapeChar="\" wildCard='%' singleChar='*'>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>pelto</ogc:Literal>
              </ogc:PropertyIsLike>
              <ogc:PropertyIsLike escapeChar="\" wildCard='%' singleChar='*'>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>maisemallisestiArvokasAlue</ogc:Literal>
              </ogc:PropertyIsLike>
            </ogc:And>
          </ogc:Filter>

          <se:Rule>            <!-- MRL AK 31 | MRL YK 41 -->
            <se:Name>Tuotantorakennusten alue, jolla on/jolle saa sijoittaa merkittävän, vaarallisia kemikaaleja valmistavan tai varastoivan laitoksen</se:Name>
            <ogc:Filter>
              <ogc:And>
                <ogc:PropertyIsLike escapeChar="\" wildCard='%' singleChar='*'>
                  <ogc:PropertyName>laji</ogc:PropertyName>
                  <ogc:Literal>tuotantorakennustenAlue</ogc:Literal>
                </ogc:PropertyIsLike>
                <ogc:PropertyIsLike escapeChar="\" wildCard='%' singleChar='*'>
                  <ogc:PropertyName>laji</ogc:PropertyName>
                  <ogc:Literal>vaarallistenKemikaalienValmistusJaVarastointiSallittu</ogc:Literal>
                </ogc:PropertyIsLike>
              </ogc:And>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#c1c3c5</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>T/kem</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>


          <se:Rule>            <!-- MRL AK 29 | MRL YK 42 -->
            <se:Name>Virkistysalue</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>virkistysAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#58ad41</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>V</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL YK 87 -->
            <se:Name>Virkistys- tai matkailukohde</se:Name>
            <ogc:Filter>
              <ogc:And>
                <ogc:PropertyIsEqualTo>
                  <ogc:Function name="dimension">
                    <ogc:PropertyName>geom</ogc:PropertyName>
                  </ogc:Function>
                  <ogc:Literal>0</ogc:Literal>
                </ogc:PropertyIsEqualTo>
                <ogc:Or>
                  <ogc:PropertyIsEqualTo>
                    <ogc:PropertyName>laji</ogc:PropertyName>
                    <ogc:Literal>virkistysAlue</ogc:Literal>
                  </ogc:PropertyIsEqualTo>
                  <ogc:PropertyIsEqualTo>
                    <ogc:PropertyName>laji</ogc:PropertyName>
                    <ogc:Literal>matkailuaPalvelevienRakennustenAlue</ogc:Literal>
                  </ogc:PropertyIsEqualTo>
                </ogc:Or>
              </ogc:And>
            </ogc:Filter>
            <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
              <se:Graphic>
                <se:Mark>
                  <se:WellKnownName>square</se:WellKnownName>
                  <se:Fill>
                    <se:SvgParameter name="fill">#58ad41</se:SvgParameter>
                  </se:Fill>
                  <se:Stroke>
                    <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                    <se:SvgParameter name="stroke-width">2</se:SvgParameter>
                  </se:Stroke>
                </se:Mark>
                <se:Size>20</se:Size>
              </se:Graphic>
            </se:PointSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 29 | MRL YK 42 -->
            <se:Name>Viheralue</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>viherAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#58ad41</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>V</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- Uusi määräys -->
            <se:Name>Ekologisen kompensaation alue</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>ekologisenKompensaationAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#58ad41</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>VX</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 34 | MRL YK 43 -->
            <se:Name>Lähivirkistysalue</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>lahiVirkistysAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#58ad41</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>VL</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 33 -->
            <se:Name>Puisto</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>puisto</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#58ad41</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>VP</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 35 -->
            <se:Name>Leikkipuisto</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>leikkiPuisto</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#58ad41</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>VK</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 36 | MRL YK 44 -->
            <se:Name>Urheilupalvelujen alue</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>urheiluPalvelujenAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#58ad41</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>VU</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 37 | MRL YK 45 -->
            <se:Name>Retkeily- ja ulkoilualue</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>retkeilyJaUlkoiluAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#58ad41</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>VR</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 38 -->
            <se:Name>Uimaranta</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>uimaranta</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#58ad41</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>VV</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 39 | MRL YK 46 -->
            <se:Name>Vapaa-ajan asumisen ja matkailun alue</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>vapaaAjanAsumisenJaMatkailunAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#ffcf45</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>R</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 40 | MRL YK 47 -->
            <se:Name>Vapaa-ajan asuinrakennusten alue</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>vapaaAjanAsuinRakennustenAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#ffcf45</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>RA</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 41 | MRL YK 48 -->
            <se:Name>Matkailua palvelevien rakennusten alue</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>matkailuaPalvelevienRakennustenAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#ffcf45</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>RM</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 42 | MRL YK 49 -->
            <se:Name>Leirintäalue</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>leirintaAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#ffcf45</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>RL</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 43 | MRL YK 50 -->
            <se:Name>Asuntovaunualue</se:Name>

            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>asuntovaunuAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#ffcf45</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>RV</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 44 | MRL YK 51 -->
            <se:Name>Siirtolapuutarha-alue</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>siirtolapuutarhaAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#ffcf45</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>RP</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 45 | MRL YK 52 -->
            <se:Name>Liikennealue</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>liikenneAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#ff0000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">12</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
              </se:Stroke>
              <se:PerpendicularOffset>6</se:PerpendicularOffset>
            </se:LineSymbolizer>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
              </se:Stroke>
              <PerpendicularOffset>2</PerpendicularOffset>
            </se:LineSymbolizer>
            <se:TextSymbolizer>
              <se:Label>L</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 46 | MRL YK 53 -->
            <se:Name>Maantie</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>maanTie</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#ff0000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">12</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
              </se:Stroke>
              <se:PerpendicularOffset>6</se:PerpendicularOffset>
            </se:LineSymbolizer>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
              </se:Stroke>
              <PerpendicularOffset>2</PerpendicularOffset>
            </se:LineSymbolizer>
            <se:TextSymbolizer>
              <se:Label>LT</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 47 | MRL YK 58 -->
            <se:Name>Rautatie</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>rautatie</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#ff0000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">12</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
              </se:Stroke>
              <se:PerpendicularOffset>6</se:PerpendicularOffset>
            </se:LineSymbolizer>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
              </se:Stroke>
              <PerpendicularOffset>2</PerpendicularOffset>
            </se:LineSymbolizer>
            <se:TextSymbolizer>
              <se:Label>LR</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 48 | MRL YK 59 -->
            <se:Name>Lentoliikenteen alue</se:Name>
            <ogc:Filter>
              <ogc:Or>
                <ogc:PropertyIsEqualTo>
                  <ogc:PropertyName>laji</ogc:PropertyName>
                  <ogc:Literal>lentoLiikenteenAlue</ogc:Literal>
                </ogc:PropertyIsEqualTo>
                <ogc:PropertyIsEqualTo>
                  <ogc:PropertyName>laji</ogc:PropertyName>
                  <ogc:Literal>lentoKentta</ogc:Literal>
                </ogc:PropertyIsEqualTo>
              </ogc:Or>
            </ogc:Filter>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#ff0000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">12</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
              </se:Stroke>
              <se:PerpendicularOffset>6</se:PerpendicularOffset>
            </se:LineSymbolizer>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
              </se:Stroke>
              <PerpendicularOffset>2</PerpendicularOffset>
            </se:LineSymbolizer>
            <se:TextSymbolizer>
              <se:Label>LL</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 49 | MRL YK 60 -->
            <se:Name>Satama</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>satama</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#ff0000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">12</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
              </se:Stroke>
              <se:PerpendicularOffset>6</se:PerpendicularOffset>
            </se:LineSymbolizer>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
              </se:Stroke>
              <PerpendicularOffset>2</PerpendicularOffset>
            </se:LineSymbolizer>
            <se:TextSymbolizer>
              <se:Label>LS</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 50 -->
            <se:Name>Kanava</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>kanava</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#ff0000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">12</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
              </se:Stroke>
              <se:PerpendicularOffset>6</se:PerpendicularOffset>
            </se:LineSymbolizer>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
              </se:Stroke>
              <PerpendicularOffset>2</PerpendicularOffset>
            </se:LineSymbolizer>
            <se:TextSymbolizer>
              <se:Label>LK</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 51 -->
            <se:Name>Venevalkama</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>veneValkama</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#ff0000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">12</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
              </se:Stroke>
              <se:PerpendicularOffset>6</se:PerpendicularOffset>
            </se:LineSymbolizer>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
              </se:Stroke>
              <PerpendicularOffset>2</PerpendicularOffset>
            </se:LineSymbolizer>
            <se:TextSymbolizer>
              <se:Label>LV</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 51 -->
            <se:Name>Venesatama</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>veneSatama</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#ff0000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">12</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
              </se:Stroke>
              <se:PerpendicularOffset>6</se:PerpendicularOffset>
            </se:LineSymbolizer>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
              </se:Stroke>
              <PerpendicularOffset>2</PerpendicularOffset>
            </se:LineSymbolizer>
            <se:TextSymbolizer>
              <se:Label>LV</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 52 -->
            <se:Name>Yleinen pysäköintialue</se:Name>
            <ogc:Filter>
              <ogc:And>
                <ogc:PropertyIsEqualTo>
                  <ogc:PropertyName>laji</ogc:PropertyName>
                  <ogc:Literal>pysakoinninAlue</ogc:Literal>
                </ogc:PropertyIsEqualTo>
                <ogc:PropertyIsEqualTo>
                  <ogc:PropertyName>lisatieto</ogc:PropertyName>
                  <ogc:Literal>varattuYleiseenKayttoon</ogc:Literal>
                </ogc:PropertyIsEqualTo>
              </ogc:And>
            </ogc:Filter>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#ff0000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">12</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
              </se:Stroke>
              <se:PerpendicularOffset>6</se:PerpendicularOffset>
            </se:LineSymbolizer>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
              </se:Stroke>
              <PerpendicularOffset>2</PerpendicularOffset>
            </se:LineSymbolizer>
            <se:TextSymbolizer>
              <se:Label>LP</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 53 -->
            <se:Name>Huoltoasema-alue</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>huoltoAsemaAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#f9c6d1</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>LH</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 54 | MRL YK 55 -->
            <se:Name>Henkilöliikenteen terminaalialue</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>henkiloLiikenteenTerminaaliAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#f9c6d1</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>LHA</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 55 | MRL YK 56 -->
            <se:Name>Tavaraliikenteen terminaalialue</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>tavaraLiikenteenTerminaaliAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#f9c6d1</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>LTA</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 56 -->
            <se:Name>Yleisten pysäköintilaitosten alue</se:Name>
            <ogc:Filter>
              <ogc:And>
                <ogc:PropertyIsEqualTo>
                  <ogc:PropertyName>laji</ogc:PropertyName>
                  <ogc:Literal>pysakointiLaitostenAlue</ogc:Literal>
                </ogc:PropertyIsEqualTo>
                <ogc:PropertyIsEqualTo>
                  <ogc:PropertyName>lisatieto</ogc:PropertyName>
                  <ogc:Literal>varattuYleiseenKayttoon</ogc:Literal>
                </ogc:PropertyIsEqualTo>
              </ogc:And>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#f9c6d1</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>LPY</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 57 -->
            <se:Name>Autopaikkojen alue</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>autoPaikkojenAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#f9c6d1</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>LPA</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 58 | MRL YK 61 -->
            <se:Name>Erityisalue</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>erityisAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#e6adcf</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>E</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 59 | MRL YK 62 -->
            <se:Name>Yhdyskuntateknisen huollon alue</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>yhdysKuntaTeknisenHuollonAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#e6adcf</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>ET</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 60 | MRL YK 63 -->
            <se:Name>Energiahuollon alue</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>energiaHuollonAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#e6adcf</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>EN</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 61 | MRL YK 64 -->
            <se:Name>Jätteenkäsittelyalue</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>jatteenKasittelyAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#e6adcf</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>EJ</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 62 | MRL YK 65 -->
            <se:Name>Maa-ainesten ottoalue</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>maaAinestenOttoAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#e6adcf</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>EO</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 63 | MRL YK 66 -->
            <se:Name>Kaivosalue</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>kaivosAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#e6adcf</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>EK</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 64 -->
            <se:Name>Mastoalue</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>mastoAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#e6adcf</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>EMT</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 65 | MRL YK 67 -->
            <se:Name>Ampumarata-alue</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>ampumaRataAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#e6adcf</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>EA</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 66 | MRL YK 68 -->
            <se:Name>Puolustusvoimien alue</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>puolustusVoimienAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#e6adcf</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>EP</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 67 | MRL YK 69 -->
            <se:Name>Hautausmaa</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>hautausMaa</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#74ccd3</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>EH</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 68 | MRL YK 70 -->
            <se:Name>Suojaviheralue</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>suojaViherAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#74ccd3</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>EV</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 69 | MRL YK 71 -->
            <se:Name>Suojelualue</se:Name>
            <ogc:Filter>
              <ogc:And>
                <ogc:PropertyIsEqualTo>
                  <ogc:Function name="dimension">
                    <ogc:PropertyName>geom</ogc:PropertyName>
                  </ogc:Function>
                  <ogc:Literal>2</ogc:Literal>
                </ogc:PropertyIsEqualTo>
                <ogc:PropertyIsEqualTo>
                  <ogc:PropertyName>laji</ogc:PropertyName>
                  <ogc:Literal>suojeluAlue</ogc:Literal>
                </ogc:PropertyIsEqualTo>
              </ogc:And>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#b6e2e3</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>S</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL YK 86 -->
            <se:Name>Suojelualue</se:Name>
            <ogc:Filter>
              <ogc:And>
                <ogc:PropertyIsEqualTo>
                  <ogc:Function name="dimension">
                    <ogc:PropertyName>geom</ogc:PropertyName>
                  </ogc:Function>
                  <ogc:Literal>0</ogc:Literal>
                </ogc:PropertyIsEqualTo>
                <ogc:Or>
                  <ogc:PropertyIsEqualTo>
                    <ogc:PropertyName>laji</ogc:PropertyName>
                    <ogc:Literal>suojeluAlue</ogc:Literal>
                  </ogc:PropertyIsEqualTo>
                  <ogc:PropertyIsEqualTo>
                    <ogc:PropertyName>laji</ogc:PropertyName>
                    <ogc:Literal>kiinteaMuinaisjaannos</ogc:Literal>
                  </ogc:PropertyIsEqualTo>
                </ogc:Or>
              </ogc:And>
            </ogc:Filter>
            <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
              <se:Graphic>
                <se:Mark>
                  <se:WellKnownName>square</se:WellKnownName>
                  <se:Fill>
                    <se:SvgParameter name="fill">#74ccd3</se:SvgParameter>
                  </se:Fill>
                  <se:Stroke>
                    <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                    <se:SvgParameter name="stroke-width">2</se:SvgParameter>
                  </se:Stroke>
                </se:Mark>
                <se:Size>20</se:Size>
              </se:Graphic>
            </se:PointSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 70 | MRL YK 72 -->
            <se:Name>Luonnonsuojelualue</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>luonnonSuojeluAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#b6e2e3</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>SL</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 71 | MRL YK 73 -->
            <se:Name>Muinaismuistoalue</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>muinaisMuistoAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#b6e2e3</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>SM</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 72 | MRL YK 74 -->
            <se:Name>Rakennussuojelualue</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>rakennusSuojeluAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#b6e2e3</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>SR</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 72 | MRL YK 74 -->
            <se:Name>Lain rakennusperinnön suojelemisesta nojalla suojeltu rakennus</se:Name>
            <ogc:Filter>
              <ogc:Or>
                <ogc:Or>
                  <ogc:PropertyIsEqualTo>
                    <ogc:PropertyName>laji</ogc:PropertyName>
                    <ogc:Literal>lainRakennusPerinnonSuojelemisestaNojallaSuojeltuRakennus</ogc:Literal>
                  </ogc:PropertyIsEqualTo>
                  <ogc:PropertyIsEqualTo>
                    <ogc:PropertyName>laji</ogc:PropertyName>
                    <ogc:Literal>kirkkoLainNojallaSuojeltuRakennus</ogc:Literal>
                  </ogc:PropertyIsEqualTo>
                </ogc:Or>
                <ogc:PropertyIsEqualTo>
                  <ogc:PropertyName>laji</ogc:PropertyName>
                  <ogc:Literal>lainOrtodoksisestaKirkostaNojallaSuojeltuRakennus</ogc:Literal>
                </ogc:PropertyIsEqualTo>
              </ogc:Or>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#b6e2e3</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>SRS</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 73 | MRL YK 76 -->
            <se:Name>Ympäristöltään säilytettävä alue</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>ymparistoltaanSailytettavaAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#ffffff</se:SvgParameter>
                <se:SvgParameter name="opacity">0.0</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>/s</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 74 | MRL YK 77 -->
            <se:Name>Maa- ja metsätalousalue</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>maaJaMetsaTalousAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#dbdb55</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>M</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 75 | MRL YK 78 -->
            <se:Name>Maatalousalue</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>maaTalousAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#eced98</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>MT</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 76 | MRL YK 79 -->
            <se:Name>Kotieläintalouden suuryksikön alue</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>kotiElainTaloudenSuurYksikonAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#c3bc03</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>ME</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 77 -->
            <se:Name>Puutarha- ja kasvihuonealue</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>puuTarhaJaKasviHuoneAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#c3bc03</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>MP</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 78 | MRL YK 80 -->
            <se:Name>Maisemallisesti arvokas peltoalue</se:Name>
            <ogc:Filter>
              <ogc:And>
                <ogc:PropertyIsLike escapeChar="\" wildCard='%' singleChar='*'>
                  <ogc:PropertyName>laji</ogc:PropertyName>
                  <ogc:Literal>pelto</ogc:Literal>
                </ogc:PropertyIsLike>
                <ogc:PropertyIsLike escapeChar="\" wildCard='%' singleChar='*'>
                  <ogc:PropertyName>laji</ogc:PropertyName>
                  <ogc:Literal>maisemallisestiArvokasAlue</ogc:Literal>
                </ogc:PropertyIsLike>
              </ogc:And>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#fff353</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>MA</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 79 | MRL YK 81 -->
            <se:Name>Maa- ja metsätalousalue, jolla on erityisiä ympäristöarvoja</se:Name>
            <ogc:Filter>
              <ogc:And>
                <ogc:PropertyIsLike escapeChar="\" wildCard='%' singleChar='*'>
                  <ogc:PropertyName>laji</ogc:PropertyName>
                  <ogc:Literal>%maaJaMetsaTalousAlue%</ogc:Literal>
                </ogc:PropertyIsLike>
                <ogc:PropertyIsLike>
                  <ogc:PropertyName>laji</ogc:PropertyName>
                  <ogc:Literal>%retkeilyJaUlkoiluAlue%</ogc:Literal>
                </ogc:PropertyIsLike>
              </ogc:And>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#bcdeb2</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>MY</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 80 | MRL YK 82 -->
            <se:Name>Maa- ja metsätalousalue, jolla on erityisiä ympäristöarvoja</se:Name>
            <ogc:Filter>
              <ogc:And>
                <ogc:PropertyIsLike escapeChar="\" wildCard='%' singleChar='*'>
                  <ogc:PropertyName>laji</ogc:PropertyName>
                  <ogc:Literal>%maaJaMetsaTalousAlue%</ogc:Literal>
                </ogc:PropertyIsLike>
                <ogc:PropertyIsLike>
                  <ogc:PropertyName>laji</ogc:PropertyName>
                  <ogc:Literal>%ymparistoarvojenHuomioiminen%</ogc:Literal>
                </ogc:PropertyIsLike>
              </ogc:And>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#bcdeb2</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>MY</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 81 | MRL YK 83 -->
            <se:Name>Vesialue</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>vesiAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#b3d7f1</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>W</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <!-- Ns. OSA-ALUEMERKINNÄT -->

          <se:Rule>            <!-- MRL AK 113 -->
            <se:Name>Rakennusala</se:Name>

            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>rakennusAla</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">1</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
                <se:SvgParameter name="stroke-dasharray">15 5 3 5</se:SvgParameter>
              </se:Stroke>
            </se:LineSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 125 -->
            <se:Name>Uloke</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>uloke</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">1</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
                <se:SvgParameter name="stroke-dasharray">15 5 3 5</se:SvgParameter>
              </se:Stroke>
            </se:LineSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 128 -->
            <se:Name>Valokatteinen tila</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>valokatteinenTila</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">1</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
                <se:SvgParameter name="stroke-dasharray">15 5 3 5 </se:SvgParameter>
              </se:Stroke>
            </se:LineSymbolizer>
            <se:TextSymbolizer>
              <se:Label>v</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">15</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">normal</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 185 | MRL YK 12 -->
            <se:Name>Maisemallisesti arvokas alue</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>maisemallisestiArvokasAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">1.5</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
                <se:SvgParameter name="stroke-dasharray">22 7 5 7</se:SvgParameter>
              </se:Stroke>
              <se:PerpendicularOffset>5</se:PerpendicularOffset>
            </se:LineSymbolizer>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">0.1</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
              </se:Stroke>
            </se:LineSymbolizer>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:GraphicFill>
                  <se:Graphic>
                    <se:Mark>
                      <se:WellKnownName>shape://horline</se:WellKnownName>
                      <se:Stroke>
                        <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                        <se:SvgParameter name="stroke-width">0.1</se:SvgParameter>
                      </se:Stroke>
                    </se:Mark>
                    <se:Size>16</se:Size>
                  </se:Graphic>
                </se:GraphicFill>
              </se:Fill>
              <se:PerpendicularOffset>-15</se:PerpendicularOffset>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>ma</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">15</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">normal</se:SvgParameter>
              </se:Font>
              <se:LabelPlacement>
                <se:LinePlacement>
                  <se:PerpendicularOffset>-8</se:PerpendicularOffset>
                </se:LinePlacement>
              </se:LabelPlacement>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 186 | MRL YK 15 -->
            <se:Name>Arvokas geologinen muodostuma</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>arvokasGeologinenMuodostuma</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">1.5</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
                <se:SvgParameter name="stroke-dasharray">22 7 5 7</se:SvgParameter>
              </se:Stroke>
              <se:PerpendicularOffset>5</se:PerpendicularOffset>
            </se:LineSymbolizer>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">0.1</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
              </se:Stroke>
            </se:LineSymbolizer>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:GraphicFill>
                  <se:Graphic>
                    <se:Mark>
                      <se:WellKnownName>shape://slash</se:WellKnownName>
                      <se:Stroke>
                        <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                        <se:SvgParameter name="stroke-width">0.1</se:SvgParameter>
                      </se:Stroke>
                    </se:Mark>
                    <se:Size>16</se:Size>
                  </se:Graphic>
                </se:GraphicFill>
              </se:Fill>
              <se:PerpendicularOffset>-8</se:PerpendicularOffset>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>ge</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">15</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">normal</se:SvgParameter>
              </se:Font>
              <se:LabelPlacement>
                <se:LinePlacement>
                  <se:PerpendicularOffset>-8</se:PerpendicularOffset>
                </se:LinePlacement>
              </se:LabelPlacement>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 187 | MRL YK 16 -->
            <se:Name>Pohjavesialue</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>pohjavesiAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">1.5</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
                <se:SvgParameter name="stroke-dasharray">22 7 5 7</se:SvgParameter>
              </se:Stroke>
              <se:PerpendicularOffset>5</se:PerpendicularOffset>
            </se:LineSymbolizer>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#b3d7f1</se:SvgParameter>
                <se:SvgParameter name="stroke-width">1</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
              </se:Stroke>
            </se:LineSymbolizer>
            <se:TextSymbolizer>
              <se:Label>pv</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">15</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">normal</se:SvgParameter>
              </se:Font>
              <se:LabelPlacement>
                <se:LinePlacement>
                  <se:PerpendicularOffset>-8</se:PerpendicularOffset>
                </se:LinePlacement>
              </se:LabelPlacement>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 189 | MRL YK 18 -->
            <se:Name>Luonnon monimuotoisuuden kannalta erityisen tärkeä alue</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>luonnonMonimuotoisuudenKannaltaTarkeaAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">1.5</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
                <se:SvgParameter name="stroke-dasharray">22 7 5 7</se:SvgParameter>
              </se:Stroke>
              <se:PerpendicularOffset>5</se:PerpendicularOffset>
            </se:LineSymbolizer>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#58ad41</se:SvgParameter>
                <se:SvgParameter name="stroke-width">1</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
              </se:Stroke>
            </se:LineSymbolizer>
            <se:TextSymbolizer>
              <se:Label>luo</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">15</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">normal</se:SvgParameter>
              </se:Font>
              <se:LabelPlacement>
                <se:LinePlacement>
                  <se:PerpendicularOffset>-8</se:PerpendicularOffset>
                </se:LinePlacement>
              </se:LabelPlacement>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 188 | MRL YK 17 -->
            <se:Name>Natura 2000 -verkoston alue</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>natura2000VerkostonAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#c4c4c4</se:SvgParameter>
                <se:SvgParameter name="stroke-width">1</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
              </se:Stroke>
            </se:LineSymbolizer>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:GraphicStroke>
                  <se:Graphic>
                    <se:Mark>
                      <se:WellKnownName>circle</se:WellKnownName>
                      <se:Fill>
                        <se:SvgParameter name="fill">#c4c4c4</se:SvgParameter>
                      </se:Fill>
                      <se:Stroke>
                        <se:SvgParameter name="stroke">#c4c4c4</se:SvgParameter>
                        <se:SvgParameter name="stroke-width">1</se:SvgParameter>
                      </se:Stroke>
                    </se:Mark>
                    <se:Size>4</se:Size>
                  </se:Graphic>
                </se:GraphicStroke>
                <se:SvgParameter name="stroke-dasharray">4 6</se:SvgParameter>
              </se:Stroke>
              <se:PerpendicularOffset>0</se:PerpendicularOffset>
            </se:LineSymbolizer>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:GraphicFill>
                  <se:Graphic>
                    <se:Mark>
                      <se:WellKnownName>shape://dot</se:WellKnownName>
                      <se:Stroke>
                        <se:SvgParameter name="stroke">#c4c4c4</se:SvgParameter>
                        <se:SvgParameter name="stroke-width">2</se:SvgParameter>
                      </se:Stroke>
                    </se:Mark>
                    <se:Size>7</se:Size>
                  </se:Graphic>
                </se:GraphicFill>
              </se:Fill>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>nat</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">15</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">normal</se:SvgParameter>
              </se:Font>
              <se:LabelPlacement>
                <se:LinePlacement>
                  <se:PerpendicularOffset>-8</se:PerpendicularOffset>
                </se:LinePlacement>
              </se:LabelPlacement>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 175 | MRL YK 24 -->
            <se:Name>Suojavyöhyke</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>suojaVyohyke</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">1.5</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
                <se:SvgParameter name="stroke-dasharray">22 7 5 7</se:SvgParameter>
              </se:Stroke>
            </se:LineSymbolizer>
            <se:TextSymbolizer>
              <se:Label>sv</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">15</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">normal</se:SvgParameter>
              </se:Font>
              <se:LabelPlacement>
                <se:LinePlacement>
                  <se:PerpendicularOffset>-8</se:PerpendicularOffset>
                </se:LinePlacement>
              </se:LabelPlacement>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 178 | MRL YK 22 -->
            <se:Name>Pilaantunut maa-alue</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>pilaantunutMaaAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">1.5</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
                <se:SvgParameter name="stroke-dasharray">22 7 5 7</se:SvgParameter>
              </se:Stroke>
            </se:LineSymbolizer>
            <se:TextSymbolizer>
              <se:Label>pima</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">15</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">normal</se:SvgParameter>
              </se:Font>
              <se:LabelPlacement>
                <se:LinePlacement>
                  <se:PerpendicularOffset>-8</se:PerpendicularOffset>
                </se:LinePlacement>
              </se:LabelPlacement>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 176 | MRL YK 111 -->
            <se:Name>Tuulivoimala-alue</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>tuuliVoimalaAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">1.5</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
                <se:SvgParameter name="stroke-dasharray">22 7 5 7</se:SvgParameter>
              </se:Stroke>
            </se:LineSymbolizer>
            <se:TextSymbolizer>
              <se:Label>tv</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">15</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">normal</se:SvgParameter>
              </se:Font>
              <se:LabelPlacement>
                <se:LinePlacement>
                  <se:PerpendicularOffset>-8</se:PerpendicularOffset>
                </se:LinePlacement>
              </se:LabelPlacement>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 177 | MRL YK 25 -->
            <se:Name>Kehittämisalue</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>kehittamisAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">1.5</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
                <se:SvgParameter name="stroke-dasharray">22 7 5 7</se:SvgParameter>
              </se:Stroke>
            </se:LineSymbolizer>
            <se:TextSymbolizer>
              <se:Label>ke</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">15</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">normal</se:SvgParameter>
              </se:Font>
              <se:LabelPlacement>
                <se:LinePlacement>
                  <se:PerpendicularOffset>-8</se:PerpendicularOffset>
                </se:LinePlacement>
              </se:LabelPlacement>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 179 | MRL YK 19  -->
            <se:Name>UNESCO:n maailmanperintökohde</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>unesconMaailmanPerintoKohde</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">1</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
              </se:Stroke>
            </se:LineSymbolizer>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:GraphicStroke>
                  <se:Graphic>
                    <se:Mark>
                      <se:WellKnownName>circle</se:WellKnownName>
                      <se:Fill>
                        <se:SvgParameter name="fill">#000000</se:SvgParameter>
                      </se:Fill>
                      <se:Stroke>
                        <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                        <se:SvgParameter name="stroke-width">1</se:SvgParameter>
                      </se:Stroke>
                    </se:Mark>
                    <se:Size>4</se:Size>
                  </se:Graphic>
                </se:GraphicStroke>
                <se:SvgParameter name="stroke-dasharray">4 6</se:SvgParameter>
              </se:Stroke>
            </se:LineSymbolizer>
            <se:TextSymbolizer>
              <se:Label>un</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">15</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">normal</se:SvgParameter>
              </se:Font>
              <se:LabelPlacement>
                <se:LinePlacement>
                  <se:PerpendicularOffset>-8</se:PerpendicularOffset>
                </se:LinePlacement>
              </se:LabelPlacement>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 180 | MRL YK 20 -->
            <se:Name>Kansallinen kaupunkipuisto</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>kansallinenKaupunkiPuisto</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">1</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
              </se:Stroke>
            </se:LineSymbolizer>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:GraphicStroke>
                  <se:Graphic>
                    <se:Mark>
                      <se:WellKnownName>circle</se:WellKnownName>
                      <se:Fill>
                        <se:SvgParameter name="fill">#000000</se:SvgParameter>
                      </se:Fill>
                      <se:Stroke>
                        <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                        <se:SvgParameter name="stroke-width">1</se:SvgParameter>
                      </se:Stroke>
                    </se:Mark>
                    <se:Size>4</se:Size>
                  </se:Graphic>
                </se:GraphicStroke>
                <se:SvgParameter name="stroke-dasharray">4 6</se:SvgParameter>
              </se:Stroke>
            </se:LineSymbolizer>
            <se:TextSymbolizer>
              <se:Label>kp</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">15</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">normal</se:SvgParameter>
              </se:Font>
              <se:LabelPlacement>
                <se:LinePlacement>
                  <se:PerpendicularOffset>-8</se:PerpendicularOffset>
                </se:LinePlacement>
              </se:LabelPlacement>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 183 -->
            <se:Name>Kiinteä muinaisjäännös</se:Name>

            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>kiinteaMuinaisjaannos</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">1.5</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
                <se:SvgParameter name="stroke-dasharray">22 7 5 7</se:SvgParameter>
              </se:Stroke>
            </se:LineSymbolizer>
            <se:TextSymbolizer>
              <se:Label>sm</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">15</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">normal</se:SvgParameter>
              </se:Font>
              <se:LabelPlacement>
                <se:LinePlacement>
                  <se:PerpendicularOffset>-8</se:PerpendicularOffset>
                </se:LinePlacement>
              </se:LabelPlacement>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 182 -->
            <se:Name>Maisemallisesti arvokas peltoalue</se:Name>
            <ogc:Filter>
              <ogc:And>
                <ogc:And>
                  <ogc:PropertyIsLike escapeChar="\" wildCard='%' singleChar='*'>
                    <ogc:PropertyName>laji</ogc:PropertyName>
                    <ogc:Literal>pelto</ogc:Literal>
                  </ogc:PropertyIsLike>
                  <ogc:PropertyIsLike escapeChar="\" wildCard='%' singleChar='*'>
                    <ogc:PropertyName>laji</ogc:PropertyName>
                    <ogc:Literal>maisemallisestiArvokasAlue</ogc:Literal>
                  </ogc:PropertyIsLike>
                </ogc:And>
                <ogc:PropertyIsEqualTo>
                  <ogc:PropertyName>lisatieto</ogc:PropertyName>
                  <ogc:Literal>osaAlue</ogc:Literal>
                </ogc:PropertyIsEqualTo>
              </ogc:And>
            </ogc:Filter>
            <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">1.5</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
                <se:SvgParameter name="stroke-dasharray">22 7 5 7</se:SvgParameter>
              </se:Stroke>
            </se:LineSymbolizer>
            <se:TextSymbolizer>
              <se:Label>mp</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">15</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">normal</se:SvgParameter>
              </se:Font>
              <se:LabelPlacement>
                <se:LinePlacement>
                  <se:PerpendicularOffset>-8</se:PerpendicularOffset>
                </se:LinePlacement>
              </se:LabelPlacement>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 181 | MRL YK 13 -->
            <se:Name>Kulttuuriympäristön kannalta arvokas alue</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>kulttuuriYmparistonKannaltaArvokasAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">1.5</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
                <se:SvgParameter name="stroke-dasharray">22 7 5 7</se:SvgParameter>
              </se:Stroke>
            </se:LineSymbolizer>
            <se:TextSymbolizer>
              <se:Label>sk</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">15</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">normal</se:SvgParameter>
              </se:Font>
              <se:LabelPlacement>
                <se:LinePlacement>
                  <se:PerpendicularOffset>-8</se:PerpendicularOffset>
                </se:LinePlacement>
              </se:LabelPlacement>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 174 | MRL YK 23 -->
            <se:Name>Vaara-alue</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>vaaraAlue</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">1.5</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
                <se:SvgParameter name="stroke-dasharray">22 7 5 7</se:SvgParameter>
              </se:Stroke>
            </se:LineSymbolizer>
            <se:TextSymbolizer>
              <se:Label>va</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">15</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">normal</se:SvgParameter>
              </se:Font>
              <se:LabelPlacement>
                <se:LinePlacement>
                  <se:PerpendicularOffset>-8</se:PerpendicularOffset>
                </se:LinePlacement>
              </se:LabelPlacement>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 120 -->
            <se:Name>Maanalainen tila</se:Name>
            <ogc:Filter>
              <ogc:And>
                <ogc:PropertyIsEqualTo>
                  <ogc:PropertyName>lisatieto</ogc:PropertyName>
                  <ogc:Literal>osaAlue</ogc:Literal>
                </ogc:PropertyIsEqualTo>
                <ogc:PropertyIsEqualTo>
                  <ogc:PropertyName>maanalaisuus</ogc:PropertyName>
                  <ogc:Literal>TRUE</ogc:Literal>
                </ogc:PropertyIsEqualTo>
              </ogc:And>
            </ogc:Filter>
            <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">1</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
                <se:SvgParameter name="stroke-dasharray">15 5 3 5</se:SvgParameter>
              </se:Stroke>
            </se:LineSymbolizer>
            <se:TextSymbolizer>
              <se:Label>ma</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">12</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">normal</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 166 -->
            <se:Name>Kunnan käyttöön varattu alue</se:Name>
            <ogc:Filter>
              <ogc:And>
                <ogc:PropertyIsLike escapeChar="\" wildCard='%' singleChar='*'>
                  <ogc:PropertyName>lisatieto</ogc:PropertyName>
                  <ogc:Literal>varattuKunnanKayttoon</ogc:Literal>
                </ogc:PropertyIsLike>
                <ogc:PropertyIsLike escapeChar="\" wildCard='%' singleChar='*'>
                  <ogc:PropertyName>lisatieto</ogc:PropertyName>
                  <ogc:Literal>osaAlue</ogc:Literal>
                </ogc:PropertyIsLike>
              </ogc:And>
            </ogc:Filter>
            <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">0.1</se:SvgParameter>
                <se:SvgParameter name="stroke-opacity">0.0</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
              </se:Stroke>
            </se:LineSymbolizer>
            <se:TextSymbolizer>
              <se:Label>/k</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">22</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">normal</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 167 -->
            <se:Name>Valtion käyttöön varattu alue</se:Name>
            <ogc:Filter>
              <ogc:And>
                <ogc:PropertyIsLike escapeChar="\" wildCard='%' singleChar='*'>
                  <ogc:PropertyName>lisatieto</ogc:PropertyName>
                  <ogc:Literal>varattuValtionKayttoon</ogc:Literal>
                </ogc:PropertyIsLike>
                <ogc:PropertyIsLike escapeChar="\" wildCard='%' singleChar='*'>
                  <ogc:PropertyName>lisatieto</ogc:PropertyName>
                  <ogc:Literal>osaAlue</ogc:Literal>
                </ogc:PropertyIsLike>
              </ogc:And>
            </ogc:Filter>
            <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">0.1</se:SvgParameter>
                <se:SvgParameter name="stroke-opacity">0.0</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
              </se:Stroke>
            </se:LineSymbolizer>
            <se:TextSymbolizer>
              <se:Label>/v</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">22</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">normal</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 168 -->
            <se:Name>Yleiseen käyttöön varattua alue</se:Name>
            <ogc:Filter>
              <ogc:And>
                <ogc:PropertyIsLike escapeChar="\" wildCard='%' singleChar='*'>
                  <ogc:PropertyName>lisatieto</ogc:PropertyName>
                  <ogc:Literal>varattuYleiseenKayttoon</ogc:Literal>
                </ogc:PropertyIsLike>
                <ogc:PropertyIsLike escapeChar="\" wildCard='%' singleChar='*'>
                  <ogc:PropertyName>lisatieto</ogc:PropertyName>
                  <ogc:Literal>osaAlue</ogc:Literal>
                </ogc:PropertyIsLike>
              </ogc:And>
            </ogc:Filter>
            <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">0.1</se:SvgParameter>
                <se:SvgParameter name="stroke-opacity">0.0</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
              </se:Stroke>
            </se:LineSymbolizer>
            <se:TextSymbolizer>
              <se:Label>/yk</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">22</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">normal</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 169 -->
            <se:Name>Suojeltava alueen osa</se:Name>
            <ogc:Filter>
              <ogc:And>
                <ogc:PropertyIsEqualTo>
                  <ogc:PropertyName>laji</ogc:PropertyName>
                  <ogc:Literal>suojeltavaAlue</ogc:Literal>
                </ogc:PropertyIsEqualTo>
                <ogc:PropertyIsEqualTo>
                  <ogc:PropertyName>lisatieto</ogc:PropertyName>
                  <ogc:Literal>osaAlue</ogc:Literal>
                </ogc:PropertyIsEqualTo>
              </ogc:And>
            </ogc:Filter>
            <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">1</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
                <se:SvgParameter name="stroke-dasharray">15 5 3 5 </se:SvgParameter>
              </se:Stroke>
            </se:LineSymbolizer>
            <se:TextSymbolizer>
              <se:Label>s</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">15</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">normal</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 170 -->
            <se:Name>Alue, jolla sijaitsee luonnonsuojelulain mukainen luonnonsuojelualue tai -kohde</se:Name>
            <ogc:Filter>
              <ogc:And>
                <ogc:PropertyIsEqualTo>
                  <ogc:PropertyName>laji</ogc:PropertyName>
                  <ogc:Literal>luonnonSuojeluAlue</ogc:Literal>
                </ogc:PropertyIsEqualTo>
                <ogc:PropertyIsEqualTo>
                  <ogc:PropertyName>lisatieto</ogc:PropertyName>
                  <ogc:Literal>osaAlue</ogc:Literal>
                </ogc:PropertyIsEqualTo>
              </ogc:And>
            </ogc:Filter>
            <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">1</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
                <se:SvgParameter name="stroke-dasharray">15 5 3 5 </se:SvgParameter>
              </se:Stroke>
            </se:LineSymbolizer>
            <se:TextSymbolizer>
              <se:Label>sl</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">15</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">normal</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 171 -->
            <se:Name>Rakennussuojelualue</se:Name>
            <ogc:Filter>
              <ogc:And>
                <ogc:PropertyIsEqualTo>
                  <ogc:PropertyName>laji</ogc:PropertyName>
                  <ogc:Literal>rakennusSuojeluAlue</ogc:Literal>
                </ogc:PropertyIsEqualTo>
                <ogc:PropertyIsEqualTo>
                  <ogc:PropertyName>lisatieto</ogc:PropertyName>
                  <ogc:Literal>osaAlue</ogc:Literal>
                </ogc:PropertyIsEqualTo>
              </ogc:And>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#b6e2e3</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>sr</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 172 -->
            <se:Name>Lain rakennusperinnön suojelemisesta nojalla suojeltu rakennus</se:Name>
            <ogc:Filter>
              <ogc:And>
                <ogc:Or>
                  <ogc:Or>
                    <ogc:PropertyIsEqualTo>
                      <ogc:PropertyName>laji</ogc:PropertyName>
                      <ogc:Literal>lainRakennusPerinnonSuojelemisestaNojallaSuojeltuRakennus</ogc:Literal>
                    </ogc:PropertyIsEqualTo>
                    <ogc:PropertyIsEqualTo>
                      <ogc:PropertyName>laji</ogc:PropertyName>
                      <ogc:Literal>kirkkoLainNojallaSuojeltuRakennus</ogc:Literal>
                    </ogc:PropertyIsEqualTo>
                  </ogc:Or>
                  <ogc:PropertyIsEqualTo>
                    <ogc:PropertyName>laji</ogc:PropertyName>
                    <ogc:Literal>lainOrtodoksisestaKirkostaNojallaSuojeltuRakennus</ogc:Literal>
                  </ogc:PropertyIsEqualTo>
                </ogc:Or>
                <ogc:PropertyIsEqualTo>
                  <ogc:PropertyName>lisatieto</ogc:PropertyName>
                  <ogc:Literal>osaAlue</ogc:Literal>
                </ogc:PropertyIsEqualTo>
              </ogc:And>
            </ogc:Filter>
            <se:PolygonSymbolizer>
              <se:Fill>
                <se:SvgParameter name="fill">#b6e2e3</se:SvgParameter>
              </se:Fill>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">4</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
              </se:Stroke>
            </se:PolygonSymbolizer>
            <se:TextSymbolizer>
              <se:Label>srs</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">bold</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 151 -->
            <se:Name>Pysäköinnin alue</se:Name>
            <ogc:Filter>
              <ogc:And>
                <ogc:PropertyIsEqualTo>
                  <ogc:PropertyName>laji</ogc:PropertyName>
                  <ogc:Literal>pysakoinninAlue</ogc:Literal>
                </ogc:PropertyIsEqualTo>
                <ogc:PropertyIsEqualTo>
                  <ogc:PropertyName>lisatieto</ogc:PropertyName>
                  <ogc:Literal>osaAlue</ogc:Literal>
                </ogc:PropertyIsEqualTo>
              </ogc:And>
            </ogc:Filter>
            <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">1</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
                <se:SvgParameter name="stroke-dasharray">15 5 3 5 </se:SvgParameter>
              </se:Stroke>
            </se:LineSymbolizer>
            <se:TextSymbolizer>
              <se:Label>p</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">15</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">normal</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 133 -->
            <se:Name>Leikki- ja/tai oleskelualueeksi varattu alue</se:Name>
            <ogc:Filter>
              <ogc:Or>
                <ogc:PropertyIsLike escapeChar="\" wildCard='%' singleChar='*'>
                  <ogc:PropertyName>laji</ogc:PropertyName>
                  <ogc:Literal>leikkiAlue</ogc:Literal>
                </ogc:PropertyIsLike>
                <ogc:PropertyIsLike escapeChar="\" wildCard='%' singleChar='*'>
                  <ogc:PropertyName>laji</ogc:PropertyName>
                  <ogc:Literal>oleskeluAlue</ogc:Literal>
                </ogc:PropertyIsLike>
              </ogc:Or>
            </ogc:Filter>
            <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">1</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
                <se:SvgParameter name="stroke-dasharray">15 5 3 5 </se:SvgParameter>
              </se:Stroke>
            </se:LineSymbolizer>
            <se:TextSymbolizer>
              <se:Label>le</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">15</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">normal</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL AK 148 -->
            <se:Name>Varattu alueen sisäiselle huoltoliikenteelle</se:Name>
            <ogc:Filter>
              <ogc:And>
                <ogc:PropertyIsEqualTo>
                  <ogc:PropertyName>laji</ogc:PropertyName>
                  <ogc:Literal>varattuHuoltoAjolle</ogc:Literal>
                </ogc:PropertyIsEqualTo>
                <ogc:PropertyIsEqualTo>
                  <ogc:PropertyName>lisatieto</ogc:PropertyName>
                  <ogc:Literal>varattuAlueenSisaiseenKayttoon</ogc:Literal>
                </ogc:PropertyIsEqualTo>
              </ogc:And>
            </ogc:Filter>
            <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
            <se:LineSymbolizer>
              <se:Stroke>
                <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                <se:SvgParameter name="stroke-width">1</se:SvgParameter>
                <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
                <se:SvgParameter name="stroke-linecap">round</se:SvgParameter>
                <se:SvgParameter name="stroke-dasharray">15 5 3 5 </se:SvgParameter>
              </se:Stroke>
            </se:LineSymbolizer>
            <se:TextSymbolizer>
              <se:Label>h</se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">15</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">normal</se:SvgParameter>
              </se:Font>
            </se:TextSymbolizer>
          </se:Rule>

          <!-- Kehittämistavoitemerkintöjä -->

          <se:Rule>            <!-- MRL YK 10 -->
            <se:Name>Ympäristö- tai maisemavaurion korjaustarve</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>ymparistoTaiMaisemaVaurionKorjausTarve</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:MaxScaleDenominator>80000</se:MaxScaleDenominator>
            <se:TextSymbolizer>
              <se:Label>
                !
              </se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">normal</se:SvgParameter>
              </se:Font>
              <se:Fill>
                <se:SvgParameter name="fill">#FFFFFF</se:SvgParameter>
              </se:Fill>
            </se:TextSymbolizer>
          </se:Rule>

          <se:Rule>            <!-- MRL YK 11 -->
            <se:Name>Terveyshaitan poistamistarve</se:Name>
            <ogc:Filter>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>laji</ogc:PropertyName>
                <ogc:Literal>terveysHaitanPoistamisTarve</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:Filter>
            <se:MaxScaleDenominator>80000</se:MaxScaleDenominator>
            <se:TextSymbolizer>
              <se:Label>
                !
              </se:Label>
              <se:Font>
                <se:SvgParameter name="font-family">Arial</se:SvgParameter>
                <se:SvgParameter name="font-size">29</se:SvgParameter>
                <se:SvgParameter name="font-style">normal</se:SvgParameter>
                <se:SvgParameter name="font-weight">normal</se:SvgParameter>
              </se:Font>
              <se:Fill>
                <se:SvgParameter name="fill">#000000</se:SvgParameter>
              </se:Fill>
            </se:TextSymbolizer>
          </se:Rule>


        </se:FeatureTypeStyle>
      </UserStyle>
    </NamedLayer>
  </StyledLayerDescriptor>