from .address import AddressDocumentViewSet, FrontAddressDocumentViewSet
from .author import AuthorDocumentViewSet
from .book import (
    BookCompoundSearchBackendDocumentViewSet,
    BookCompoundSearchBoostSearchBackendDocumentViewSet,
    BookDefaultFilterLookupDocumentViewSet,
    BookDocumentViewSet,
    BookCustomDocumentViewSet,
    BookFrontendDocumentViewSet,
    BookFunctionalSuggesterDocumentViewSet,
    BookIgnoreIndexErrorsDocumentViewSet,
    BookMoreLikeThisDocumentViewSet,
    BookMoreLikeThisNoOptionsDocumentViewSet,
    BookMultiMatchOptionsPhasePrefixSearchFilterBackendDocumentViewSet,
    BookMultiMatchSearchFilterBackendDocumentViewSet,
    BookOrderingByScoreCompoundSearchBackendDocumentViewSet,
    BookOrderingByScoreDocumentViewSet,
    BookPermissionsDocumentViewSet,
    BookSimpleQueryStringBoostSearchFilterBackendDocumentViewSet,
    BookSimpleQueryStringSearchFilterBackendDocumentViewSet,
    BookSourceSearchBackendDocumentViewSet,
)
from .city import CityDocumentViewSet, CityCompoundSearchBackendDocumentViewSet
from .location import LocationDocumentViewSet
from .publisher import PublisherDocumentViewSet

__all__ = (
    'AddressDocumentViewSet',
    'AuthorDocumentViewSet',
    'BookCompoundSearchBackendDocumentViewSet',
    'BookCompoundSearchBoostSearchBackendDocumentViewSet',
    'BookDefaultFilterLookupDocumentViewSet',
    'BookDocumentViewSet',
    'BookCustomDocumentViewSet',
    'BookFrontendDocumentViewSet',
    'BookFunctionalSuggesterDocumentViewSet',
    'BookIgnoreIndexErrorsDocumentViewSet',
    'BookMoreLikeThisDocumentViewSet',
    'BookMoreLikeThisNoOptionsDocumentViewSet',
    'BookMultiMatchOptionsPhasePrefixSearchFilterBackendDocumentViewSet',
    'BookMultiMatchSearchFilterBackendDocumentViewSet',
    'BookOrderingByScoreCompoundSearchBackendDocumentViewSet',
    'BookOrderingByScoreDocumentViewSet',
    'BookPermissionsDocumentViewSet',
    'BookSimpleQueryStringBoostSearchFilterBackendDocumentViewSet',
    'BookSimpleQueryStringSearchFilterBackendDocumentViewSet',
    'BookSourceSearchBackendDocumentViewSet',
    'CityCompoundSearchBackendDocumentViewSet',
    'CityDocumentViewSet',
    'LocationDocumentViewSet',
    'PublisherDocumentViewSet',
    'FrontAddressDocumentViewSet',
)
