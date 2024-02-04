import json
from time import sleep
import websockets
import asyncio
import polyline
 
# The main function that will handle connection and communication
# with the server

geometry = "}_tnA_kzgNTBIyC@q@?_AFaBZ{DPcBLwAJu@LkBRmCb@kAzAiFDyACi@MkM?w@Hs@TmA~@mDtAoFn@oB`A_C`BeDR]d@y@v@aBTm@L]rAgEb@wARk@^i@h@oALc@RmA\\wALe@FWv@cD^oBZeB@W@[@_@E_@[sAa@aAMYTIT_@d@_DNm@h@mB`AkDh@wBXo@H[r@uBV{@~@cDp@_ChAcExBcH`@kAtAuDRe@r@uBfAiDh@mBf@uCtAwFZ_Af@cBFUFW@Eh@sBtCoJ`@wAb@}Ad@iB`@qBPoAr@qI~@mNl@cH@OnAwP`@sEBqIAiD?OEcAGgIAsB?qDFkARq@Xm@V{@pAiDpCaHJQX{@Vo@P{@@o@GsAC{@Cw@@aALiA?e@@_AD}@No@vBoEnBoEnBgEl@uAzCyGxD}I|FaMvB}Eh@kAVk@z@kB~DcJxD_IrBuEvCqGrFuLrDkIfByDf@}@Tk@|ByERc@LS`AqB~@cEPo@N[t@u@h@WvFqCh@_@zAwABGfAaCp@{AhEsJXm@HMjCwF~BcFfAgBl@o@x@m@`Ag@pOoIZM^Kf@E~DCVE`A[hAg@HODg@Bm@@UAqBGeBEuB?cH@qAEy@DkADqA@UJgDKaA@gA?KEMKO]O]Ao@Bc@@GaAv@C~@Kf@MPINOJFH@RCbAKfBG?EBEFAFF?FCBn@b@NTJ\\HJPJvAd@d@t@p@~@RX@Br@dBZf@vAtAT^n@\\dARfBV\\FbDf@b@J\\Jt@b@bBIZ?rFBjABrD?f@?\\CrDUt@SxBg@d@IlD_@|AMv@CpCGXAbAA~@ADHBX@fCAfBr@n@dA|@fCzAxBn@XCfAgD|@}BPQx@u@d@i@Z{@Vq@Nu@^w@jABv@{AfA{BjAaCV{@f@iBPuAXmCzAP~AJdCThAJdAJv@HbAH\\BdAFlAHzADdBHT@tAJp@HxBJnAF`AJrAPnALrAFnAFrABd@BdAPT?\\m@pH{Kd@u@TPk@p@kHzKW`@`@?bFv@tARR@hANx@J\\D|@HLBvBd@H?d@@lAVbAMh@KdAa@ZCpBLtBRzBRvACTmCXgELeCHcAF_@Ha@`@oFfAFl@yIR?fAgOk@INiBLuALgA{Fw@_@GICQMOKlJeLr@cAdAiBV[`@[XYJSJ_@HUN_@XIL?zAd@^mG\\{FDm@BoAFm@Bc@Lq@GQq@[c@KmBN}@Ha@JWPc@jACZuCq@@WfAgDb@}ABQBk@Am@Ss@]}@e@oAwAaC{AoB}HaIwC}CwCuCsBqBQKwAm@m@[iBaBuDyDmHyHa@e@QWK_@A[j@AvAGCSiBkCsBuE}@qDi@gDSuDAwELg@KeAFeADQZuARgABsAKwAUyA}@}DWuBASLA|Em@dC_@vEy@xEo@bGy@vB]zAOvEq@p@M`L_BpCe@b@E`C]tJu@|G{@nA[HSdBn@~Al@`I|CxE~ArDrAfEpAZHhAVvAb@dBj@b@NrC`ArC~@PFjHzBtBj@vDbAr@NrEdAHB~GxAlHvBvGnBnB|@^RRN~AbBpDjEp@r@RNX\\l@d@RJd@Z`A\\n@NjANrIzApE|AxSdI`KtDZH|DlAdCr@t@NvA\\|HvAh@HdAP|@JrCRdBHxE^l@DzF^nBJd@DvDVnAJjM~@jIh@zJr@pEV~ANpDXrBLJ@t_@zCvBRbDVlCNrFNhGNzR`@R@zADpCFdJTfLV|JR`H`@xPFhGBjCNlAHhHnAfANt@?hDDlBCbQEtHEnBGfDQxAC|CKD?V?vEDvGd@dEN`@@?RAJO?"
cordinates = polyline.decode(geometry, 5)
# print(cordinates)

async def ws_client():
    print("WebSocket: Client Connected.")
    url = "ws://192.168.29.180:8000/ws/buslocation/4"
    # Connect to the server
    async with websockets.connect(url) as ws:

       
        for cor in cordinates:
            loc = { "lat" : cor[0], "lang" : cor[1] }
            await ws.send(json.dumps(loc))
            msg = await ws.recv()
            print(msg)
            # sleep(1)
 
        
        # while True:
        #     msg = await ws.recv()
        #     print(msg)
 
# Start the connection
asyncio.run(ws_client())