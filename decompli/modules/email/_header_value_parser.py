# Module: _header_value_parser
# Pseudo-source reconstructed from bytecode (no decompiler)


def quote_string(value):
    ...

def TokenList():
    """TokenList"""
    ...

def WhiteSpaceTokenList():
    """WhiteSpaceTokenList"""
    ...

def UnstructuredTokenList():
    """UnstructuredTokenList"""
    ...

def Phrase():
    """Phrase"""
    ...

def Word():
    """Word"""
    ...

def CFWSList():
    """CFWSList"""
    ...

def Atom():
    """Atom"""
    ...

def Token():
    """Token"""
    ...

def EncodedWord():
    """EncodedWord"""
    ...

def QuotedString():
    """QuotedString"""
    ...

def BareQuotedString():
    """BareQuotedString"""
    ...

def Comment():
    """Comment"""
    ...

def AddressList():
    """AddressList"""
    ...

def Address():
    """Address"""
    ...

def MailboxList():
    """MailboxList"""
    ...

def GroupList():
    """GroupList"""
    ...

def Group():
    """Group"""
    ...

def NameAddr():
    """NameAddr"""
    ...

def AngleAddr():
    """AngleAddr"""
    ...

def ObsRoute():
    """ObsRoute"""
    ...

def Mailbox():
    """Mailbox"""
    ...

def InvalidMailbox():
    """InvalidMailbox"""
    ...

def Domain():
    """Domain"""
    ...

def DotAtom():
    """DotAtom"""
    ...

def DotAtomText():
    """DotAtomText"""
    ...

def NoFoldLiteral():
    """NoFoldLiteral"""
    ...

def AddrSpec():
    """AddrSpec"""
    ...

def ObsLocalPart():
    """ObsLocalPart"""
    ...

def DisplayName():
    """DisplayName"""
    ...

def LocalPart():
    """LocalPart"""
    ...

def DomainLiteral():
    """DomainLiteral"""
    ...

def MIMEVersion():
    """MIMEVersion"""
    ...

def Parameter():
    """Parameter"""
    ...

def InvalidParameter():
    """InvalidParameter"""
    ...

def Attribute():
    """Attribute"""
    ...

def Section():
    """Section"""
    ...

def Value():
    """Value"""
    ...

def MimeParameters():
    """MimeParameters"""
    ...

def ParameterizedHeaderValue():
    """ParameterizedHeaderValue"""
    ...

def ContentType():
    """ContentType"""
    ...

def ContentDisposition():
    """ContentDisposition"""
    ...

def ContentTransferEncoding():
    """ContentTransferEncoding"""
    ...

def HeaderLabel():
    """HeaderLabel"""
    ...

def MsgID():
    """MsgID"""
    ...

def MessageID():
    """MessageID"""
    ...

def InvalidMessageID():
    """InvalidMessageID"""
    ...

def Header():
    """Header"""
    ...

def Terminal():
    """Terminal"""
    ...

def WhiteSpaceTerminal():
    """WhiteSpaceTerminal"""
    ...

def ValueTerminal():
    """ValueTerminal"""
    ...

def EWWhiteSpaceTerminal():
    """EWWhiteSpaceTerminal"""
    ...

def _InvalidEwError():
    """_InvalidEwError"""
    ...

def _validate_xtext(xtext):
    """If input token contains ASCII non-printables, register a defect."""
    ...

def _get_ptext_to_endchars(value, endchars):
    """
    Scan printables/quoted-pairs until endchars and return unquoted ptext.
    
        This function turns a run of qcontent, ccontent-without-comments, or
        dtext-with-quoted-printables into a single string by unquoting any
        quoted printables.  It returns the string, the remaining value, and
        a flag that is True iff there were any quoted printables decoded.
    
        
    """
    ...

def get_fws(value):
    """
    FWS = 1*WSP
    
        This isn't the RFC definition.  We're using fws to represent tokens where
        folding can be done, but when we are parsing the *un*folding has already
        been done so we don't need to watch out for CRLF.
    
        
    """
    ...

def get_encoded_word(value):
    """
     encoded-word = "=?" charset "?" encoding "?" encoded-text "?="
    
        
    """
    ...

def get_unstructured(value):
    """
    unstructured = (*([FWS] vchar) *WSP) / obs-unstruct
           obs-unstruct = *((*LF *CR *(obs-utext) *LF *CR)) / FWS)
           obs-utext = %d0 / obs-NO-WS-CTL / LF / CR
    
           obs-NO-WS-CTL is control characters except WSP/CR/LF.
    
        So, basically, we have printable runs, plus control characters or nulls in
        the obsolete syntax, separated by whitespace.  Since RFC 2047 uses the
        obsolete syntax in its specification, but requires whitespace on either
        side of the encoded words, I can see no reason to need to separate the
        non-printable-non-whitespace from the printable runs if they occur, so we
        parse this into xtext tokens separated by WSP tokens.
    
        Because an 'unstructured' value must by definition constitute the entire
        value, this 'get' routine does not return a remaining value, only the
        parsed TokenList.
    
        
    """
    ...

def get_qp_ctext(value):
    """
    ctext = <printable ascii except \ ( )>
    
        This is not the RFC ctext, since we are handling nested comments in comment
        and unquoting quoted-pairs here.  We allow anything except the '()'
        characters, but if we find any ASCII other than the RFC defined printable
        ASCII, a NonPrintableDefect is added to the token's defects list.  Since
        quoted pairs are converted to their unquoted values, what is returned is
        a 'ptext' token.  In this case it is a WhiteSpaceTerminal, so it's value
        is ' '.
    
        
    """
    ...

def get_qcontent(value):
    """
    qcontent = qtext / quoted-pair
    
        We allow anything except the DQUOTE character, but if we find any ASCII
        other than the RFC defined printable ASCII, a NonPrintableDefect is
        added to the token's defects list.  Any quoted pairs are converted to their
        unquoted values, so what is returned is a 'ptext' token.  In this case it
        is a ValueTerminal.
    
        
    """
    ...

def get_atext(value):
    """
    atext = <matches _atext_matcher>
    
        We allow any non-ATOM_ENDS in atext, but add an InvalidATextDefect to
        the token's defects list if we find non-atext characters.
        
    """
    ...

def get_bare_quoted_string(value):
    """
    bare-quoted-string = DQUOTE *([FWS] qcontent) [FWS] DQUOTE
    
        A quoted-string without the leading or trailing white space.  Its
        value is the text between the quote marks, with whitespace
        preserved and quoted pairs decoded.
        
    """
    ...

def get_comment(value):
    """
    comment = "(" *([FWS] ccontent) [FWS] ")"
           ccontent = ctext / quoted-pair / comment
    
        We handle nested comments here, and quoted-pair in our qp-ctext routine.
        
    """
    ...

def get_cfws(value):
    """
    CFWS = (1*([FWS] comment) [FWS]) / FWS
    
        
    """
    ...

def get_quoted_string(value):
    """
    quoted-string = [CFWS] <bare-quoted-string> [CFWS]
    
        'bare-quoted-string' is an intermediate class defined by this
        parser and not by the RFC grammar.  It is the quoted string
        without any attached CFWS.
        
    """
    ...

def get_atom(value):
    """
    atom = [CFWS] 1*atext [CFWS]
    
        An atom could be an rfc2047 encoded word.
        
    """
    ...

def get_dot_atom_text(value):
    """
     dot-text = 1*atext *("." 1*atext)
    
        
    """
    ...

def get_dot_atom(value):
    """
     dot-atom = [CFWS] dot-atom-text [CFWS]
    
        Any place we can have a dot atom, we could instead have an rfc2047 encoded
        word.
        
    """
    ...

def get_word(value):
    """
    word = atom / quoted-string
    
        Either atom or quoted-string may start with CFWS.  We have to peel off this
        CFWS first to determine which type of word to parse.  Afterward we splice
        the leading CFWS, if any, into the parsed sub-token.
    
        If neither an atom or a quoted-string is found before the next special, a
        HeaderParseError is raised.
    
        The token returned is either an Atom or a QuotedString, as appropriate.
        This means the 'word' level of the formal grammar is not represented in the
        parse tree; this is because having that extra layer when manipulating the
        parse tree is more confusing than it is helpful.
    
        
    """
    ...

def get_phrase(value):
    """
     phrase = 1*word / obs-phrase
            obs-phrase = word *(word / "." / CFWS)
    
        This means a phrase can be a sequence of words, periods, and CFWS in any
        order as long as it starts with at least one word.  If anything other than
        words is detected, an ObsoleteHeaderDefect is added to the token's defect
        list.  We also accept a phrase that starts with CFWS followed by a dot;
        this is registered as an InvalidHeaderDefect, since it is not supported by
        even the obsolete grammar.
    
        
    """
    ...

def get_local_part(value):
    """
     local-part = dot-atom / quoted-string / obs-local-part
    
        
    """
    ...

def get_obs_local_part(value):
    """
     obs-local-part = word *("." word)
        
    """
    ...

def get_dtext(value):
    """
     dtext = <printable ascii except \ [ ]> / obs-dtext
            obs-dtext = obs-NO-WS-CTL / quoted-pair
    
        We allow anything except the excluded characters, but if we find any
        ASCII other than the RFC defined printable ASCII, a NonPrintableDefect is
        added to the token's defects list.  Quoted pairs are converted to their
        unquoted values, so what is returned is a ptext token, in this case a
        ValueTerminal.  If there were quoted-printables, an ObsoleteHeaderDefect is
        added to the returned token's defect list.
    
        
    """
    ...

def _check_for_early_dl_end(value, domain_literal):
    ...

def get_domain_literal(value):
    """
     domain-literal = [CFWS] "[" *([FWS] dtext) [FWS] "]" [CFWS]
    
        
    """
    ...

def get_domain(value):
    """
     domain = dot-atom / domain-literal / obs-domain
            obs-domain = atom *("." atom))
    
        
    """
    ...

def get_addr_spec(value):
    """
     addr-spec = local-part "@" domain
    
        
    """
    ...

def get_obs_route(value):
    """
     obs-route = obs-domain-list ":"
            obs-domain-list = *(CFWS / ",") "@" domain *("," [CFWS] ["@" domain])
    
            Returns an obs-route token with the appropriate sub-tokens (that is,
            there is no obs-domain-list in the parse tree).
        
    """
    ...

def get_angle_addr(value):
    """
     angle-addr = [CFWS] "<" addr-spec ">" [CFWS] / obs-angle-addr
            obs-angle-addr = [CFWS] "<" obs-route addr-spec ">" [CFWS]
    
        
    """
    ...

def get_display_name(value):
    """
     display-name = phrase
    
        Because this is simply a name-rule, we don't return a display-name
        token containing a phrase, but rather a display-name token with
        the content of the phrase.
    
        
    """
    ...

def get_name_addr(value):
    """
     name-addr = [display-name] angle-addr
    
        
    """
    ...

def get_mailbox(value):
    """
     mailbox = name-addr / addr-spec
    
        
    """
    ...

def get_invalid_mailbox(value, endchars):
    """
     Read everything up to one of the chars in endchars.
    
        This is outside the formal grammar.  The InvalidMailbox TokenList that is
        returned acts like a Mailbox, but the data attributes are None.
    
        
    """
    ...

def get_mailbox_list(value):
    """
     mailbox-list = (mailbox *("," mailbox)) / obs-mbox-list
            obs-mbox-list = *([CFWS] ",") mailbox *("," [mailbox / CFWS])
    
        For this routine we go outside the formal grammar in order to improve error
        handling.  We recognize the end of the mailbox list only at the end of the
        value or at a ';' (the group terminator).  This is so that we can turn
        invalid mailboxes into InvalidMailbox tokens and continue parsing any
        remaining valid mailboxes.  We also allow all mailbox entries to be null,
        and this condition is handled appropriately at a higher level.
    
        
    """
    ...

def get_group_list(value):
    """
     group-list = mailbox-list / CFWS / obs-group-list
            obs-group-list = 1*([CFWS] ",") [CFWS]
    
        
    """
    ...

def get_group(value):
    """
     group = display-name ":" [group-list] ";" [CFWS]
    
        
    """
    ...

def get_address(value):
    """
     address = mailbox / group
    
        Note that counter-intuitively, an address can be either a single address or
        a list of addresses (a group).  This is why the returned Address object has
        a 'mailboxes' attribute which treats a single address as a list of length
        one.  When you need to differentiate between to two cases, extract the single
        element, which is either a mailbox or a group token.
    
        
    """
    ...

def get_address_list(value):
    """
     address_list = (address *("," address)) / obs-addr-list
            obs-addr-list = *([CFWS] ",") address *("," [address / CFWS])
    
        We depart from the formal grammar here by continuing to parse until the end
        of the input, assuming the input to be entirely composed of an
        address-list.  This is always true in email parsing, and allows us
        to skip invalid addresses to parse additional valid ones.
    
        
    """
    ...

def get_no_fold_literal(value):
    """
     no-fold-literal = "[" *dtext "]"
        
    """
    ...

def get_msg_id(value):
    """
    msg-id = [CFWS] "<" id-left '@' id-right  ">" [CFWS]
           id-left = dot-atom-text / obs-id-left
           id-right = dot-atom-text / no-fold-literal / obs-id-right
           no-fold-literal = "[" *dtext "]"
        
    """
    ...

def parse_message_id(value):
    """
    message-id      =   "Message-ID:" msg-id CRLF
        
    """
    ...

def parse_mime_version(value):
    """
     mime-version = [CFWS] 1*digit [CFWS] "." [CFWS] 1*digit [CFWS]
    
        
    """
    ...

def get_invalid_parameter(value):
    """
     Read everything up to the next ';'.
    
        This is outside the formal grammar.  The InvalidParameter TokenList that is
        returned acts like a Parameter, but the data attributes are None.
    
        
    """
    ...

def get_ttext(value):
    """
    ttext = <matches _ttext_matcher>
    
        We allow any non-TOKEN_ENDS in ttext, but add defects to the token's
        defects list if we find non-ttext characters.  We also register defects for
        *any* non-printables even though the RFC doesn't exclude all of them,
        because we follow the spirit of RFC 5322.
    
        
    """
    ...

def get_token(value):
    """
    token = [CFWS] 1*ttext [CFWS]
    
        The RFC equivalent of ttext is any US-ASCII chars except space, ctls, or
        tspecials.  We also exclude tabs even though the RFC doesn't.
    
        The RFC implies the CFWS but is not explicit about it in the BNF.
    
        
    """
    ...

def get_attrtext(value):
    """
    attrtext = 1*(any non-ATTRIBUTE_ENDS character)
    
        We allow any non-ATTRIBUTE_ENDS in attrtext, but add defects to the
        token's defects list if we find non-attrtext characters.  We also register
        defects for *any* non-printables even though the RFC doesn't exclude all of
        them, because we follow the spirit of RFC 5322.
    
        
    """
    ...

def get_attribute(value):
    """
     [CFWS] 1*attrtext [CFWS]
    
        This version of the BNF makes the CFWS explicit, and as usual we use a
        value terminal for the actual run of characters.  The RFC equivalent of
        attrtext is the token characters, with the subtraction of '*', "'", and '%'.
        We include tab in the excluded set just as we do for token.
    
        
    """
    ...

def get_extended_attrtext(value):
    """
    attrtext = 1*(any non-ATTRIBUTE_ENDS character plus '%')
    
        This is a special parsing routine so that we get a value that
        includes % escapes as a single string (which we decode as a single
        string later).
    
        
    """
    ...

def get_extended_attribute(value):
    """
     [CFWS] 1*extended_attrtext [CFWS]
    
        This is like the non-extended version except we allow % characters, so that
        we can pick up an encoded value as a single string.
    
        
    """
    ...

def get_section(value):
    """
     '*' digits
    
        The formal BNF is more complicated because leading 0s are not allowed.  We
        check for that and add a defect.  We also assume no CFWS is allowed between
        the '*' and the digits, though the RFC is not crystal clear on that.
        The caller should already have dealt with leading CFWS.
    
        
    """
    ...

def get_value(value):
    """
     quoted-string / attribute
    
        
    """
    ...

def get_parameter(value):
    """
     attribute [section] ["*"] [CFWS] "=" value
    
        The CFWS is implied by the RFC but not made explicit in the BNF.  This
        simplified form of the BNF from the RFC is made to conform with the RFC BNF
        through some extra checks.  We do it this way because it makes both error
        recovery and working with the resulting parse tree easier.
        
    """
    ...

def parse_mime_parameters(value):
    """
     parameter *( ";" parameter )
    
        That BNF is meant to indicate this routine should only be called after
        finding and handling the leading ';'.  There is no corresponding rule in
        the formal RFC grammar, but it is more convenient for us for the set of
        parameters to be treated as its own TokenList.
    
        This is 'parse' routine because it consumes the remaining value, but it
        would never be called to parse a full header.  Instead it is called to
        parse everything after the non-parameter value of a specific MIME header.
    
        
    """
    ...

def _find_mime_parameters(tokenlist, value):
    """
    Do our best to find the parameters in an invalid MIME header
    
        
    """
    ...

def parse_content_type_header(value):
    """
     maintype "/" subtype *( ";" parameter )
    
        The maintype and substype are tokens.  Theoretically they could
        be checked against the official IANA list + x-token, but we
        don't do that.
        
    """
    ...

def parse_content_disposition_header(value):
    """
     disposition-type *( ";" parameter )
    
        
    """
    ...

def parse_content_transfer_encoding_header(value):
    """
     mechanism
    
        
    """
    ...

def _steal_trailing_WSP_if_exists(lines):
    ...

def _refold_parse_tree(parse_tree, *, policy=None):
    """
    Return string of contents of parse_tree folded according to RFC rules.
    
        
    """
    ...

def _fold_as_ew(to_encode, lines, maxlen, last_ew, ew_combine_allowed, charset):
    """
    Fold string to_encode into lines as encoded word, combining if allowed.
        Return the new value for last_ew, or None if ew_combine_allowed is False.
    
        If there is already an encoded word in the last line of lines (indicated by
        a non-None value for last_ew) and ew_combine_allowed is true, decode the
        existing ew, combine it with to_encode, and re-encode.  Otherwise, encode
        to_encode.  In either case, split to_encode as necessary so that the
        encoded segments fit within maxlen.
    
        
    """
    ...

def _fold_mime_parameters(part, lines, maxlen, encoding):
    """
    Fold TokenList 'part' into the 'lines' list as mime parameters.
    
        Using the decoded list of parameters and values, format them according to
        the RFC rules, including using RFC2231 encoding if the value cannot be
        expressed in 'encoding' and/or the parameter+value is too long to fit
        within 'maxlen'.
    
        
    """
    ...
