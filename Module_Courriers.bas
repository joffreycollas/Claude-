Attribute VB_Name = "Module_Courriers"
'=====================================================================
' Publipostage - Courrier d'augmentation tarifaire
' Onglets requis : "Clients" (en-tetes ligne 1) et "Courrier"
' Nom defini requis : Client_Selectionne (cellule Courrier!I3)
'=====================================================================
Option Explicit

Private Const COL_CODE As String = "A"
Private Const COL_SOCIETE As String = "E"
Private Const COL_ENVOI As String = "X"
Private Const COL_MODE As String = "Y"

' Un PDF par client (A envoyer = Oui) dans le sous-dossier Courriers_PDF
Public Sub ExporterTousLesPDF()
    Dim wsC As Worksheet, wsL As Worksheet
    Dim dossier As String, fichier As String, codeInitial As Variant
    Dim i As Long, derniere As Long, nb As Long

    Set wsC = ThisWorkbook.Worksheets("Clients")
    Set wsL = ThisWorkbook.Worksheets("Courrier")
    dossier = DossierSortie()
    If dossier = "" Then Exit Sub

    codeInitial = wsL.Range("Client_Selectionne").Value
    Application.ScreenUpdating = False
    derniere = wsC.Cells(wsC.Rows.Count, COL_CODE).End(xlUp).Row

    For i = 2 To derniere
        If AEnvoyer(wsC, i) Then
            wsL.Range("Client_Selectionne").Value = wsC.Cells(i, COL_CODE).Value
            Application.Calculate
            fichier = dossier & Application.PathSeparator & "Courrier_" & _
                      NettoyerNom(wsC.Cells(i, COL_CODE).Value & "_" & wsC.Cells(i, COL_SOCIETE).Value) & ".pdf"
            wsL.ExportAsFixedFormat Type:=xlTypePDF, Filename:=fichier, _
                Quality:=xlQualityStandard, IncludeDocProperties:=False, _
                IgnorePrintAreas:=False, OpenAfterPublish:=False
            nb = nb + 1
        End If
    Next i

    wsL.Range("Client_Selectionne").Value = codeInitial
    Application.ScreenUpdating = True
    MsgBox nb & " courrier(s) exporte(s) en PDF dans :" & vbCrLf & dossier, vbInformation
End Sub

' Un seul PDF regroupant tous les courriers (A envoyer = Oui)
Public Sub ExporterUnSeulPDF()
    Dim wsC As Worksheet, wsL As Worksheet, wbTmp As Workbook, ws As Worksheet
    Dim dossier As String, codeInitial As Variant
    Dim i As Long, derniere As Long, nb As Long

    Set wsC = ThisWorkbook.Worksheets("Clients")
    Set wsL = ThisWorkbook.Worksheets("Courrier")
    dossier = DossierSortie()
    If dossier = "" Then Exit Sub

    codeInitial = wsL.Range("Client_Selectionne").Value
    Application.ScreenUpdating = False
    Application.DisplayAlerts = False
    derniere = wsC.Cells(wsC.Rows.Count, COL_CODE).End(xlUp).Row

    For i = 2 To derniere
        If AEnvoyer(wsC, i) Then
            wsL.Range("Client_Selectionne").Value = wsC.Cells(i, COL_CODE).Value
            Application.Calculate
            If wbTmp Is Nothing Then
                wsL.Copy
                Set wbTmp = ActiveWorkbook
            Else
                wsL.Copy After:=wbTmp.Sheets(wbTmp.Sheets.Count)
            End If
            Set ws = wbTmp.Sheets(wbTmp.Sheets.Count)
            ws.UsedRange.Copy
            ws.UsedRange.PasteSpecial Paste:=xlPasteValues
            Application.CutCopyMode = False
            ws.Name = Left(NettoyerNom(CStr(wsC.Cells(i, COL_CODE).Value)), 25) & "_" & i
            nb = nb + 1
        End If
    Next i

    If nb > 0 Then
        wbTmp.ExportAsFixedFormat Type:=xlTypePDF, _
            Filename:=dossier & Application.PathSeparator & "Courriers_augmentation_TOUS.pdf", _
            Quality:=xlQualityStandard, IncludeDocProperties:=False, _
            IgnorePrintAreas:=False, OpenAfterPublish:=True
        wbTmp.Close SaveChanges:=False
    End If

    wsL.Range("Client_Selectionne").Value = codeInitial
    Application.DisplayAlerts = True
    Application.ScreenUpdating = True
    MsgBox nb & " courrier(s) regroupe(s) dans Courriers_augmentation_TOUS.pdf", vbInformation
End Sub

' Impression papier : A envoyer = Oui ET Mode d'envoi = Courrier ou Les deux
Public Sub ImprimerCourriersPostaux()
    Dim wsC As Worksheet, wsL As Worksheet, codeInitial As Variant
    Dim i As Long, derniere As Long, nb As Long, mode As String

    Set wsC = ThisWorkbook.Worksheets("Clients")
    Set wsL = ThisWorkbook.Worksheets("Courrier")
    If MsgBox("Lancer l'impression des courriers postaux sur l'imprimante par defaut ?", _
              vbYesNo + vbQuestion) = vbNo Then Exit Sub

    codeInitial = wsL.Range("Client_Selectionne").Value
    derniere = wsC.Cells(wsC.Rows.Count, COL_CODE).End(xlUp).Row

    For i = 2 To derniere
        mode = LCase(Trim(CStr(wsC.Cells(i, COL_MODE).Value)))
        If AEnvoyer(wsC, i) And (mode = "courrier" Or mode = "les deux" Or mode = "") Then
            wsL.Range("Client_Selectionne").Value = wsC.Cells(i, COL_CODE).Value
            Application.Calculate
            wsL.PrintOut Copies:=1
            nb = nb + 1
        End If
    Next i

    wsL.Range("Client_Selectionne").Value = codeInitial
    MsgBox nb & " courrier(s) envoye(s) a l'imprimante.", vbInformation
End Sub

'--------------------------------------------------------------------- utilitaires
Private Function AEnvoyer(wsC As Worksheet, ByVal i As Long) As Boolean
    AEnvoyer = Trim(CStr(wsC.Cells(i, COL_CODE).Value)) <> "" And _
               LCase(Trim(CStr(wsC.Cells(i, COL_ENVOI).Value))) = "oui"
End Function

Private Function DossierSortie() As String
    Dim d As String
    If ThisWorkbook.Path = "" Then
        MsgBox "Enregistrez d'abord le classeur (format .xlsm).", vbExclamation
        Exit Function
    End If
    d = ThisWorkbook.Path & Application.PathSeparator & "Courriers_PDF"
    If Dir(d, vbDirectory) = "" Then MkDir d
    DossierSortie = d
End Function

Private Function NettoyerNom(ByVal s As String) As String
    Dim c As Variant
    For Each c In Array("\", "/", ":", "*", "?", """", "<", ">", "|", "[", "]", "'")
        s = Replace(s, c, "")
    Next c
    NettoyerNom = Trim(Replace(s, " ", "_"))
End Function
